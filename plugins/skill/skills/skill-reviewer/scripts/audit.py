#!/usr/bin/env python3
"""Mechanical checks for a skill directory. Judgment stays with the reviewer.

    audit.py <skill-dir> [--json]

Reports what can be decided by reading the files alone: sizes, the heading
tree, pointers that go nowhere, files nothing points to, frontmatter fields,
and prose density. Anything that needs to weigh a reader's need is left out.
"""
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

POINTER = re.compile(r"\[[^\]]*\]\(([^)]+)\)|`([^`]*\.(?:md|py|sh|js|ts|json|ya?ml))`")
# コードブロックの中で呼んでいる scripts/ も「指している」に数える
PATH_IN_CODE = re.compile(r"[\w./${}-]*?((?:references|scripts|assets)/[\w./-]+)")


def frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    head, body = text[3:end], text[end + 4 :]
    out = {}
    for line in head.splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out, body


def sections(text):
    """Heading, level and how many lines sit under it."""
    lines = text.splitlines()
    marks = [(i, m.group(1), m.group(2)) for i, l in enumerate(lines)
             if (m := re.match(r"^(#{1,6}) (.+)$", l))]
    out = []
    for n, (i, hashes, title) in enumerate(marks):
        end = marks[n + 1][0] if n + 1 < len(marks) else len(lines)
        out.append({"level": len(hashes), "title": title, "line": i + 1, "lines": end - i - 1})
    return out


def audit(root: Path):
    skill = root / "SKILL.md"
    if not skill.exists():
        sys.exit(f"no SKILL.md in {root}")
    text = skill.read_text()
    fm, body = frontmatter(text)
    supporting = sorted(p for p in root.rglob("*") if p.is_file() and p.name != "SKILL.md")

    pointed = {m.group(1) for m in PATH_IN_CODE.finditer(text)}
    for m in POINTER.finditer(text):
        target = m.group(1) or m.group(2)
        if target and not target.startswith(("http://", "https://")):
            pointed.add(target.split("#")[0].strip())

    findings = []
    if (n := len(text.splitlines())) > 500:
        findings.append(("size", f"SKILL.md is {n} lines; inspect whether conditional detail belongs in references (heuristic)"))

    if not re.match(r"^---[ \t]*\r?\n", text):
        findings.append(("frontmatter", "missing opening frontmatter delimiter on line 1"))
    elif not re.search(r"^---[ \t]*$", text.split("\n", 1)[1], re.M):
        findings.append(("frontmatter", "missing closing frontmatter delimiter"))
    elif yaml is None:
        findings.append(("validation", "PyYAML unavailable; YAML validity was not checked"))
    else:
        head = re.split(r"^---[ \t]*$", text, maxsplit=2, flags=re.M)[1]
        try:
            parsed = yaml.safe_load(head)
            if not isinstance(parsed, dict):
                findings.append(("frontmatter", "frontmatter must be a YAML mapping"))
            else:
                fm = parsed
        except yaml.YAMLError as e:
            findings.append(("frontmatter", f"YAML does not parse: {e}"))

    for target in sorted(pointed):
        if not target.startswith(("references/", "scripts/", "assets/")):
            continue
        if (root / target).exists():
            continue
        # リポジトリ側の scripts/ を指していることがある。上へ辿って見つかれば skill の欠落ではない
        if any((parent / target).exists() for parent in root.parents):
            continue
        findings.append(("pointer", f"`{target}` is pointed to but does not exist"))

    for p in supporting:
        rel = p.relative_to(root).as_posix()
        if not any(rel.endswith(t) or t.endswith(rel) for t in pointed):
            findings.append(("orphan", f"`{rel}` has no direct pointer from SKILL.md; check references and host discovery before treating it as orphaned"))

    files = [skill] + [p for p in supporting if p.suffix == ".md"]
    sizes = {p.relative_to(root).as_posix(): len(p.read_text().splitlines()) for p in files}

    tree = {}
    for p in files:
        rel = p.relative_to(root).as_posix()
        tree[rel] = sections(p.read_text())
        same = [s for s in tree[rel] if s["level"] == 2]
        if len(same) > 2:
            longest, median = max(s["lines"] for s in same), sorted(s["lines"] for s in same)[len(same) // 2]
            if median and longest > median * 3:
                big = max(same, key=lambda s: s["lines"])
                findings.append(("proportion",
                                 f"{rel}: `{big['title']}` is {big['lines']} lines against a median of {median}"))

    prose = {}
    for p in files:
        t = p.read_text()
        rel = p.relative_to(root).as_posix()
        prose[rel] = {
            "bold": t.count("**") // 2,
            "imperatives": len(re.findall(r"\b(MUST|ALWAYS|NEVER)\b", t)),
            "lines": sizes[rel],
        }
        if prose[rel]["imperatives"] > 3:
            findings.append(("prose", f"{rel}: {prose[rel]['imperatives']} uses of MUST/ALWAYS/NEVER"))
        if sizes[rel] > 20 and prose[rel]["bold"] > sizes[rel] / 3:
            findings.append(("prose", f"{rel}: {prose[rel]['bold']} bold spans in {sizes[rel]} lines"))

    return {"skill": root.name, "frontmatter": fm, "sizes": sizes, "headings": tree,
            "prose": prose, "findings": [{"kind": k, "detail": d} for k, d in findings]}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    root = Path(args[0] if args else ".").expanduser().resolve()
    result = audit(root)
    if "--json" in sys.argv:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return
    print(f"# {result['skill']}\n")
    for rel, n in result["sizes"].items():
        print(f"{n:5}  {rel}")
    print()
    for rel, secs in result["headings"].items():
        print(rel)
        for s in secs:
            print(f"  {'  ' * (s['level'] - 1)}{s['title']}  ({s['lines']} 行)")
    print()
    if not result["findings"]:
        print("mechanical checks: nothing to report")
        return
    for f in result["findings"]:
        print(f"[{f['kind']}] {f['detail']}")


if __name__ == "__main__":
    main()
