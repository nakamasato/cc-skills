# 見出しコーパス (一次データ)

実在する OSS / 公開技術ドキュメントから収集した H2 / H3 の逐語リスト。
`section-vocabulary.md` / `heading-forms.md` / `ja-heading-glossary.md` の主張は
すべてこのファイルの実例に対応する。**ここに無い見出しを「よくある形」として
書かないこと。**

収集は WebFetch / WebSearch による。取得できなかった URL は各節末尾の
`## FAILED` に理由つきで残してある（件数は水増ししていない）。

書式: `H2:` は出現順の逐語リスト、`H3:` は代表例（最大6件）。

内訳: 英語 80 件 / 日本語 37 件（うち railsguides getting_started と
readouble Laravel installation は 2 回収集されており、ユニークは 35 件）。
## React — installation
URL: https://raw.githubusercontent.com/reactjs/react.dev/main/src/content/learn/installation.md
H2: Try React | Creating a React App | Build a React App from Scratch | Add React to an existing project | Next steps
H3: Should I use Create React App?

## Vue — getting-started
URL: https://raw.githubusercontent.com/vuejs/docs/main/src/guide/quick-start.md
H2: Try Vue Online | Creating a Vue Application | Using Vue from CDN | Frameworks | Next Steps
H3: Using the Global Build | Using the ES Module Build | Enabling Import maps | Splitting Up the Modules

## Angular — installation
URL: https://angular.dev/installation
H2: Installation | Play Online | Set up a new project locally | Next steps | Social Media | Community | Resources | Community translations
H3: Prerequisites | Instructions | Install Angular CLI | Create a new project | Running your new project locally | Using AI for Development

## SvelteKit — getting-started
URL: https://raw.githubusercontent.com/sveltejs/kit/main/documentation/docs/10-getting-started/10-introduction.md
H2: Before we begin | What is SvelteKit? | What is Svelte? | SvelteKit vs Svelte
H3: (none)

## Next.js — installation
URL: https://raw.githubusercontent.com/vercel/next.js/canary/docs/01-app/01-getting-started/01-installation.mdx
H2: Quick start | System requirements | Supported browsers | Create with the CLI | Manual installation | Create the `public` folder (optional) | Run the development server | Set up TypeScript | Set up your editor | Set up linting | Set up Absolute Imports and Module Path Aliases | Upgrade your Next.js app
H3: Create the `app` directory | Create the `pages` directory | IDE Plugin

## Django — tutorial
URL: https://raw.githubusercontent.com/django/django/main/docs/intro/tutorial01.txt
H2 (RST top-level, "=" underline): Writing your first Django app, part 1 | Creating a project | The development server | Creating the Polls app | Write your first view
H3: (none — no "-"-underlined sub-headings in this section of the doc)

## Django — deployment
URL: https://docs.djangoproject.com/en/stable/howto/deployment/checklist/
H2: Deployment checklist | Run `manage.py check --deploy` | Switch away from `manage.py runserver` | Critical settings | Environment-specific settings | HTTPS | Performance optimizations | Error reporting
H3: `SECRET_KEY` | `DEBUG` | `ALLOWED_HOSTS` | `CACHES` | `DATABASES` | `MAILERS` and related settings

## Flask — guide
URL: https://raw.githubusercontent.com/pallets/flask/main/docs/quickstart.rst
H2 (RST top-level, "=" underline): Quickstart | A Minimal Application | Debug Mode | HTML Escaping | Routing | Static Files | Rendering Templates | Accessing Request Data | Redirects and Errors | About Responses | Sessions | Message Flashing | Logging | Hooking in WSGI Middleware | Using Flask Extensions | Deploying to a Web Server
H3 (RST sub-level, "-" underline, sample): Variable Rules | Unique URLs / Redirection Behavior | URL Building | HTTP Methods | File Uploads | Cookies

## FastAPI — tutorial
URL: https://raw.githubusercontent.com/fastapi/fastapi/master/docs/en/docs/tutorial/index.md
H2: Tutorial - User Guide | Run the code | Install FastAPI | AI Agent Skills | Advanced User Guide
H3: (none)

## Ruby on Rails — getting-started
URL: https://raw.githubusercontent.com/rails/rails/main/guides/source/getting_started.md
H2: Getting Started with Rails | Introduction | Rails Philosophy | Creating a New Rails App | Hello, Rails! | Creating a Database Model | Rails Console | Active Record Model Basics | A Request's Journey Through Rails | Routes | Controllers & Actions | Adding Authentication | Caching Products | Rich Text Fields with Action Text | File Uploads with Active Storage | Internationalization (I18n) | Action Mailer and Email Notifications | Adding CSS & JavaScript | Testing | Consistently Formatted Code with RuboCop | Security | Continuous Integration with `bin/ci` | Deploying to Production
H3 (sample, first 6): Prerequisites | Creating Your First Rails App | Directory Structure | Model-View-Controller Basics | Database Migrations | Running Migrations
NOTE: extracted by an automated markdown-to-heading pass, not manually diffed line-by-line against the raw file — treat H3 list as indicative rather than exhaustive/precisely ordered.

## Laravel — installation
URL: https://raw.githubusercontent.com/laravel/docs/master/installation.md
H2: Meet Laravel | Why Laravel? | Creating a Laravel Application | Installing PHP and the Laravel Installer | Creating an Application | Initial Configuration | Environment Based Configuration | Databases and Migrations | Directory Configuration | Installation Using Herd | Herd on macOS | Herd on Windows | IDE Support | Laravel and AI | Installing Laravel Boost | Next Steps | Laravel the Full Stack Framework | Laravel the API Backend
H3 (sample, first 6): Why Laravel? | A Progressive Framework | A Scalable Framework | An Agent Ready Framework | A Community Framework | Installing PHP and the Laravel Installer

## Spring Boot — tutorial
URL: https://docs.spring.io/spring-boot/tutorial/first-application/index.html
H2: Developing Your First Spring Boot Application | Prerequisites | Setting Up the Project With Maven | Setting Up the Project With Gradle | Adding Classpath Dependencies | Writing the Code | Running the Example | Creating an Executable Jar
H3 (sample, first 6): Maven | Gradle | The @RestController and @RequestMapping Annotations | The @SpringBootApplication Annotation | The "main" Method | Maven

## Express — installation
URL: https://expressjs.com/en/starter/installing.html
H2: Installing | TypeScript
H3: Warning | Note

## Rust Book — installation
URL: https://raw.githubusercontent.com/rust-lang/book/main/src/ch01-01-installation.md
H2: Installation
H3: Command Line Notation | Installing `rustup` on Linux or macOS | Installing `rustup` on Windows | Troubleshooting | Updating and Uninstalling | Reading the Local Documentation

## Go — guide (Effective Go)
URL: https://go.dev/doc/effective_go
H2: Introduction | Formatting | Commentary | Names | Semicolons | Control structures | Functions | Data | Initialization | Methods | Interfaces and other types | The blank identifier | Embedding | Concurrency | Errors
H3 (sample, first 6): Indentation | Line length | Parentheses | Package names | Getters | Interface names

## Node.js — api-reference (Synopsis)
URL: https://nodejs.org/api/synopsis.html
H2: Usage and example
H3: Usage | Example

## Deno — installation
URL: https://raw.githubusercontent.com/denoland/docs/main/runtime/getting_started/installation.md
H2: Download and install | Manual download | Docker | Installation location | Testing your installation | Updating | Uninstalling | Building from source
H3 (sample, first 4): Cross-platform package managers | Binary location | Cache location | If you see "command not found"

## Astro — installation
URL: https://raw.githubusercontent.com/withastro/docs/main/src/content/docs/en/install-and-setup.mdx
H2: Prerequisites | Browser compatibility | Install from the CLI wizard | CLI installation flags | Manual Setup
H3: Add integrations | Use a theme or starter template

## Nuxt — installation
URL: https://nuxt.com/docs/4.x/getting-started/installation
H2: Installation | Play Online | New Project | Next Steps | Sitemap
H3: Prerequisites | Create a New Project | Development Server

## RubyGems — guide (Make your own gem)
URL: https://raw.githubusercontent.com/rubygems/guides/gh-pages/make-your-own-gem.md
H2: Introduction | Your first gem | Starting with bundle gem | Requiring more files | Using other gems | Writing tests | Adding an executable | Documenting your code | Releasing your gem | Wrapup | Credits
H3: Testing with Minitest | Testing with RSpec | With gem push | With rake release

## Phoenix — installation
URL: https://raw.githubusercontent.com/phoenixframework/phoenix/main/guides/introduction/installation.md
H2: Installation | Elixir 1.18 or later | Erlang 27 or later | Phoenix | PostgreSQL | inotify-tools (for Linux users) | Summary
H3: (none)

## FAILED
- Vue quick-start: none (succeeded)
- Nuxt raw GitHub markdown (https://raw.githubusercontent.com/nuxt/nuxt.com/main/content/3.docs/1.getting-started/2.installation.md and https://raw.githubusercontent.com/nuxt/nuxt/main/docs/1.getting-started/2.installation.md): 404 — repo/path restructured; recovered via WebFetch on the live docs site (https://nuxt.com/docs/4.x/getting-started/installation) instead, listed above.
- Express raw GitHub markdown (https://raw.githubusercontent.com/expressjs/expressjs.com/gh-pages/en/starter/installing.md and .../master/en/starter/installing.md): 404 — recovered via WebFetch on the live docs site (https://expressjs.com/en/starter/installing.html) instead, listed above.
- Spring Boot raw GitHub asciidoc (https://raw.githubusercontent.com/spring-projects/spring-boot/main/spring-boot-project/spring-boot-docs/src/docs/antora/modules/getting-started/pages/introducing-spring-boot.adoc): 404 — antora doc path restructured; recovered via WebFetch on the live docs site (https://docs.spring.io/spring-boot/tutorial/first-application/index.html) instead, listed above.
- Node.js raw GitHub markdown (https://raw.githubusercontent.com/nodejs/node/main/doc/api/synopsis.md): 404 — recovered via WebFetch on the live docs site (https://nodejs.org/api/synopsis.html) instead, listed above.
- Rust Book ch01-00-getting-started.md: fetched successfully but page is a stub with only an H1 title and no H2/H3 content; substituted ch01-01-installation.md (listed above) as the representative installation doc for this chapter.
## Kubernetes — reference (kubectl cheat sheet)
URL: https://raw.githubusercontent.com/kubernetes/website/main/content/en/docs/reference/kubectl/quick-reference.md
H2: Kubectl autocomplete | Kubectl context and configuration | Kubectl apply | Creating objects | Viewing and finding resources | Updating resources | Patching resources | Editing resources | Scaling resources | Deleting resources | Interacting with running Pods | Copying files and directories to and from containers | Interacting with Deployments and Services | Interacting with Nodes and cluster
H3: BASH | ZSH | FISH | A note on `--all-namespaces` | Resource types | Formatting output

## Kubernetes — troubleshooting
URL: https://raw.githubusercontent.com/kubernetes/website/main/content/en/docs/tasks/debug/debug-application/debug-running-pod.md
H2: Using `kubectl describe pod` to fetch details about pods | Example: debugging Pending Pods | Examining pod logs | Debugging with container exec | Debugging with an ephemeral debug container | Debugging using a copy of the Pod | Debugging via a shell on the node | Debugging a Pod or Node while applying a profile
H3: Example debugging using ephemeral containers | Copying a Pod while adding a new container | Copying a Pod while changing its command | Copying a Pod while changing container images | Applying a Static Profile | Applying Custom Profile

## Kubernetes — troubleshooting
URL: https://raw.githubusercontent.com/kubernetes/website/main/content/en/docs/tasks/debug/debug-cluster/_index.md
H2: Listing your cluster | Looking at logs | Cluster failure modes
H3: Example: debugging a down/unreachable node | Control Plane nodes | Worker Nodes | Contributing causes | Specific scenarios | Mitigations

## etcd — configuration
URL: https://raw.githubusercontent.com/etcd-io/website/main/content/en/docs/v3.6/op-guide/configuration.md
H2: Configuration options | Command-line flags | Configuration file
H3: Member | Clustering | Security | Auth | Profiling and monitoring | Logging

## containerd — operations
URL: https://raw.githubusercontent.com/containerd/containerd/main/docs/ops.md
H2: systemd | Base Configuration | Plugin Configuration
H3: Bolt Metadata Plugin

## ArgoCD — troubleshooting
URL: https://raw.githubusercontent.com/argoproj/argo-cd/master/docs/operator-manual/troubleshooting.md
H2: Settings | Cluster credentials
H3: (none found)

## Grafana — configuration
URL: https://raw.githubusercontent.com/grafana/grafana/main/docs/sources/setup-grafana/configure-grafana/_index.md
H2: Configure Grafana | Customize your Grafana instance | Configuration file location | Remove comments in the .ini files | Override configuration with environment variables | Variable expansion | Configuration options
H3: `app_mode` | `instance_name` | `[paths]` | `[server]` | `[server.custom_response_headers]` | `[database]`

## Prometheus — configuration
URL: https://raw.githubusercontent.com/prometheus/prometheus/main/docs/configuration/configuration.md
H2: Configuration file | `<scrape_config>` | `<http_config>` | `<tls_config>` | `<oauth2>` | `<aws_sd_config>` | `<azure_sd_config>` | `<consul_sd_config>` | `<digitalocean_sd_config>` | `<docker_sd_config>` | `<dockerswarm_sd_config>` | `<dns_sd_config>` | `<ec2_sd_config>`
H3: `<scrape_config>` | `<http_config>` | `<tls_config>` | `<oauth2>` | `<aws_sd_config>` | `<azure_sd_config>`

## Prometheus — guide (querying basics)
URL: https://raw.githubusercontent.com/prometheus/prometheus/main/docs/querying/basics.md
H2: Examples | Samples | Expression language data types | Reconciliation of histogram bucket layouts | Literals | Time series selectors | Subquery | Operators | Functions | Comments | Regular expressions | Gotchas
H3: String literals | Float literals and time durations | Duration expressions | Instant vector selectors | Range Vector Selectors | Offset modifier

## GitHub Actions — troubleshooting
URL: https://raw.githubusercontent.com/github/docs/main/content/actions/how-tos/troubleshoot-workflows.md
H2: Initial troubleshooting suggestions | Reviewing billing errors | Reviewing {% data variables.product.prodname_actions %} activity with metrics | Troubleshooting workflow triggers | Troubleshoot workflow execution | Troubleshooting runners | Networking troubleshooting suggestions
H3: Using {% data variables.product.prodname_copilot %} | Using workflow run logs | Enabling debug logging | Setting a budget | Triggering event conditions | Scheduled workflows running at unexpected times

## Istio — troubleshooting
URL: https://raw.githubusercontent.com/istio/istio.io/master/content/en/docs/ops/common-problems/network-issues/index.md
H2: Requests are rejected by Envoy | Route rules don't seem to affect traffic flow | 503 errors after setting destination rule | Route rules have no effect on ingress gateway requests | Envoy is crashing under load | Envoy won't connect to my HTTP/1.0 service | 503 error while accessing headless services | TLS configuration mistakes | Unchanged Envoy filter configuration suddenly stops working | Virtual service with fault injection and retry/timeout policies not working as expected
H3: Sending HTTPS to an HTTP port | Gateway to virtual service TLS mismatch | Gateway with TLS termination | Gateway with TLS passthrough | Double TLS (TLS origination for a TLS request) | 404 errors occur when multiple gateways configured with same TLS certificate

## cert-manager — troubleshooting
URL: https://raw.githubusercontent.com/cert-manager/website/master/content/docs/troubleshooting/acme.md
H2: Overview | 1. Troubleshooting (Cluster)Issuers | 2. Troubleshooting Orders | 3. Troubleshooting Challenges | March 2020 Let's Encrypt CAA Rechecking Bug
H3: Common errors | Common errors | HTTP01 troubleshooting | Got 404 status code | Got 503 status code | DNS01 troubleshooting

## Vault — configuration
URL: https://developer.hashicorp.com/vault/docs/configuration
H2: Vault configuration parameters | Parameters | High availability parameters | Vault enterprise parameters
H3: Configuration stanzas | VAULT + AI | Resources

## Terraform — configuration (CLI config file)
URL: https://developer.hashicorp.com/terraform/cli/config/config-file
H2: Introduction | Locations | Configuration File Syntax | Available Settings | Credentials | Provider Installation | Removed Settings
H3: Environment Variable Credentials | Credentials Helpers | Credentials Source Priority Order | Explicit Installation Method Configuration | Implied Local Mirror Directories | Provider Plugin Cache

## Consul — troubleshooting
URL: https://developer.hashicorp.com/consul/docs/troubleshoot
H2: Troubleshoot Consul datacenter operations | Workflow | Where to start | Kubernetes deployments | External troubleshooting tools | Next steps
H3: Cluster members | Raft peers | Agent log output | Validate configuration | Generate debug file | Latest health check status

## PostgreSQL — configuration
URL: https://www.postgresql.org/docs/current/runtime-config-connection.html
H2: 19.3. Connections and Authentication
H3: 19.3.1. Connection Settings | 19.3.2. TCP Settings | 19.3.3. Authentication | 19.3.4. SSL

## Ansible — faq
URL: https://docs.ansible.com/ansible/latest/reference_appendices/faq.html
H2: Frequently Asked Questions | Where did all the modules go? | Where did this specific module go? | How can I speed up Ansible on systems with slow disks? | How can I set the PATH or any other environment variable for a task or entire play? | How do I handle different machines needing different user accounts or ports to log in with? | How do I get ansible to reuse connections, enable Kerberized SSH, or have Ansible pay attention to my local SSH config file? | How do I configure a jump host to access servers that I have no direct access to? | How do I get Ansible to notice a dead target in a timely manner? | How do I speed up run of ansible for servers from cloud providers (EC2, openstack,.. )? | How do I handle not having a Python interpreter at /usr/bin/python on a remote machine? | How do I handle the package dependencies required by Ansible package dependencies during Ansible installation ? | Common System Issues | What is the best way to make content reusable/redistributable? | Where does the configuration file live and what can I configure in it? | How do I disable cowsay? | How do I see a list of all of the ansible_ variables? | How do I see all the inventory variables defined for my host? | How do I see all the variables specific to my host? | How do I loop over a list of hosts in a group, inside of a template? | How do I access a variable name programmatically? | How do I access a group variable? | How do I access a variable of the first host in a group? | How do I copy files recursively onto a target host? | How do I access shell environment variables? | How do I generate encrypted passwords for the user module? | Ansible allows dot notation and array notation for variables. Which notation should I use? | When is it unsafe to bulk-set task arguments from a variable? | Can I get training on Ansible? | Is there a web interface / REST API / GUI? | How do I keep secret data in my playbook? | When should I use {{ }}? Also, how to interpolate variables or dynamic variable names | How do I get the original ansible_host when I delegate a task? | How do I fix 'protocol error: file name does not match request' when fetching a file? | Does Ansible support multiple factor authentication 2FA/MFA/biometrics/finterprint/usbkey/OTP/… | The 'validate' option is not enough for my needs, what do I do? | How do I submit a change to the documentation? | What is the difference between `ansible.legacy` and `ansible.builtin` collections? | I don't see my question here
H3: Running in a virtualenv | Running on macOS as a control node | Running on macOS as a target | Running on BSD | Running on Solaris | Running on z/OS

## Elasticsearch — troubleshooting
URL: https://www.elastic.co/guide/en/elasticsearch/reference/current/troubleshooting.html
H2: General | Data | Management | Capacity | Snapshot and restore | Other issues | Additional resources
H3: (none found — subsection items are bullet points, not H3 headings)

## MySQL — troubleshooting (InnoDB)
URL: https://dev.mysql.com/doc/refman/8.0/en/innodb-troubleshooting.html
H2: 17.21 InnoDB Troubleshooting
H3: 17.21.1 Troubleshooting InnoDB I/O Problems | 17.21.2 Troubleshooting Recovery Failures | 17.21.3 Forcing InnoDB Recovery | 17.21.4 Troubleshooting InnoDB Data Dictionary Operations | 17.21.5 InnoDB Error Handling

## HAProxy — configuration
URL: https://www.haproxy.com/documentation/haproxy-configuration-manual/latest/
H2: Quick reminder about HTTP | Configuring HAProxy | Global section | Proxies | Bind and server options | Cache | Using ACLs and fetching samples | Logging | Supported filters | FastCGI applications | Stick-tables and Peers | Other sections
H3: The HTTP transaction model | Terminology | HTTP request | HTTP response | The Request line | The request headers

## FAILED
- https://raw.githubusercontent.com/docker/docs/main/content/reference/compose-file/_index.md — fetched OK but page has no real H2/H3 markdown headings (nav/index page only); excluded from results.
- https://raw.githubusercontent.com/docker/docs/main/content/engine/daemon/_index.md — HTTP 404
- https://raw.githubusercontent.com/docker/docs/main/content/engine/daemon/troubleshoot.md — HTTP 404
- https://raw.githubusercontent.com/prometheus/docs/main/docs/prometheus/latest/configuration/configuration.md — HTTP 404 (wrong path; found correct doc under prometheus/prometheus repo instead)
- https://raw.githubusercontent.com/prometheus/docs/main/docs/prometheus/latest/querying/basics.md — HTTP 404 (same, superseded)
- https://raw.githubusercontent.com/grafana/grafana/main/docs/sources/setup-grafana/configure-grafana/index.md — HTTP 404 (wrong filename; `_index.md` succeeded instead)
- https://raw.githubusercontent.com/helm/helm-www/main/content/en/docs/chart_template_guide/debugging.md — HTTP 404
- https://raw.githubusercontent.com/helm/helm-www/main/content/en/docs/topics/charts_hooks.md — HTTP 404
- https://raw.githubusercontent.com/redis/docs/main/content/operate/oss_and_stack/management/troubleshooting.md — fetched OK but page has no H2 headings (only H1 title + two H3s); excluded from results.
- https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/docs/plugins/README.md — HTTP 404
- https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/docs/plugins.md — HTTP 404
- https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/docs/FAQ.md — HTTP 404
- https://github.com/kubernetes-sigs/kustomize/tree/master/docs — HTTP 404 (could not enumerate directory to find a working doc path)
- https://raw.githubusercontent.com/istio/istio.io/master/content/en/docs/ops/common-problems/network-issues.md — HTTP 404 (wrong path; `.../network-issues/index.md` succeeded instead)
- https://raw.githubusercontent.com/envoyproxy/envoy/main/docs/root/faq/overview.rst — fetched but content was a toctree of linked doc titles, not real page headings; excluded as unreliable.
- https://raw.githubusercontent.com/envoyproxy/envoy/main/docs/root/operations/admin.rst — fetched but result mixed Sphinx `:ref:` anchor labels with headings, not verbatim page headings; excluded as unreliable.
- https://nginx.org/en/docs/http/ngx_http_core_module.html — fetched OK but page is a flat directive reference (no real H2/H3 structure); excluded.
- https://www.postgresql.org/docs/current/runtime-config.html — fetched OK but only one H2 (chapter title) with TOC links, not real H3 elements; superseded by runtime-config-connection.html which has real H3s.
- https://dev.mysql.com/doc/refman/8.4/en/replication-troubleshooting.html — HTTP 404 (8.4 refman path doesn't exist)
- https://dev.mysql.com/doc/refman/8.0/en/replication-troubleshooting.html — HTTP 404
- https://dev.mysql.com/doc/refman/8.0/en/problems.html — fetched OK but page has no H2 headings (only H3s); excluded, superseded by innodb-troubleshooting.html.
- https://kafka.apache.org/documentation/#operations — fetched OK but WebFetch only received the site nav/redirect shell, not the actual single-page doc content.
- https://kafka.apache.org/39/documentation.html — same issue, nav shell only, actual chapter content not retrievable via WebFetch.
- https://kafka.apache.org/documentation.html — same issue.
- https://raw.githubusercontent.com/apache/kafka/trunk/docs/ops.html — HTTP 404
- https://www.elastic.co/docs/troubleshoot/elasticsearch/index — HTTP 404 (new docs site path wrong; classic guide URL succeeded instead)
## facebook/react — README
URL: https://raw.githubusercontent.com/facebook/react/main/README.md
H2: Installation | Documentation | Examples | Contributing
H3: [Code of Conduct](https://code.fb.com/codeofconduct) | [Contributing Guide](https://legacy.reactjs.org/docs/how-to-contribute.html) | [Good First Issues](https://github.com/facebook/react/labels/good%20first%20issue) | License

## vuejs/core — README
URL: https://raw.githubusercontent.com/vuejs/core/main/README.md
H2: Getting Started | Sponsors | Questions | Issues | Stay In Touch | Contribution | License
H3: (none)

## denoland/deno — README
URL: https://raw.githubusercontent.com/denoland/deno/main/README.md
H2: Installation | Your first Deno program | Additional resources | Contributing
H3: Build and install from source

## kubernetes/kubernetes — README
URL: https://raw.githubusercontent.com/kubernetes/kubernetes/master/README.md
H2: To start using K8s | To start developing K8s | Support | Community Meetings | Adopters | Governance | Roadmap
H3: (none)

## prometheus/prometheus — README
URL: https://raw.githubusercontent.com/prometheus/prometheus/main/README.md
H2: Architecture overview | Install | Using Prometheus as a Go Library | React UI Development | More information | Contributing | License
H3: Precompiled binaries | Docker images | Building from source | Service discovery plugins | Building the Docker image | Remote Write

## ohmyzsh/ohmyzsh — README
URL: https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/README.md
H2: Getting Started | Using Oh My Zsh | Advanced Topics | Getting Updates | Uninstalling Oh My Zsh | How Do I Contribute To Oh My Zsh? | Contributors | Follow Us | Merchandise | License | About Planet Argon
H3: Operating System Compatibility | Prerequisites | Basic Installation | Plugins | Themes | FAQ

## fastapi/fastapi — README
URL: https://raw.githubusercontent.com/fastapi/fastapi/master/README.md
H2: Sponsors | Opinions | FastAPI mini documentary | **Typer**, the FastAPI of CLIs | Requirements | Installation | Example | Example upgrade | Performance | Dependencies | License
H3: Keystone Sponsor | Gold Sponsors | Silver Sponsors | Create it | Run it | Check it

## vuejs/core — contributing
URL: https://raw.githubusercontent.com/vuejs/core/main/.github/contributing.md
H2: Issue Reporting Guidelines | Pull Request Guidelines | Development Setup | Git Hooks | Scripts | Project Structure | Contributing Tests | Financial Contribution | Credits
H3: What kinds of Pull Requests are accepted? | Pull Request Checklist | Advanced Pull Request Tips | `nr build` | `nr build-dts` | `nr check`

## prometheus/prometheus — contributing
URL: https://raw.githubusercontent.com/prometheus/prometheus/main/CONTRIBUTING.md
H2: Steps to Contribute | Pull Request Checklist | Dependency management | Working with the PromQL parser
H3: (none)

## rust-lang/rust — contributing
URL: https://raw.githubusercontent.com/rust-lang/rust/master/CONTRIBUTING.md
H2: Making changes to subtrees and submodules | About the [rustc-dev-guide] | LLM policy | [Getting help](https://rustc-dev-guide.rust-lang.org/getting-started.html#asking-questions) | Bug reports
H3: (none)

## hashicorp/terraform — contributing
URL: https://raw.githubusercontent.com/hashicorp/terraform/main/.github/CONTRIBUTING.md
H2: Introduction | Contributing a Pull Request | Proposing a Change | Terraform CLI/Core Development Environment | Acceptance Tests: Testing interactions with external services | Generated Code | External Dependencies | AI Usage
H3: Caveats & areas of special concern | Pull Request Lifecycle | PR Checks | Transparency | Accountability | Quality

## nodejs/node — security
URL: https://raw.githubusercontent.com/nodejs/node/main/SECURITY.md
H2: Reporting a bug in Node.js | Reporting a bug in a third-party module | Disclosure policy | Code of Conduct and Vulnerability Reporting Guidelines | The Node.js threat model | Receiving security updates | Comments on this policy | Incident Response Plan | Node.js Security Team | Team responsible for Triaging security reports | Team with access to private security reports against Node.js | Team with access to private security patches to Node.js
H3: Node.js bug bounty program | Experimental platforms | Experimental features behind compile-time flags, experimental runtime flags, and V8 flags | Security triage dispositions | What constitutes a vulnerability | Examples of vulnerabilities

## electron/electron — security
URL: https://raw.githubusercontent.com/electron/electron/main/SECURITY.md
H2: Escalation | The Electron Security Notification Process | Learning More About Security
H3: (none)

## axios/axios — security
URL: https://raw.githubusercontent.com/axios/axios/v1.x/SECURITY.md
H2: Supported versions | Threat model | Verifying a release | Reporting a vulnerability | Reporting process | Disclosure policy | Security updates | Security partners and acknowledgements
H3: 60-day resolution and disclosure commitment

## joelparkerhenderson/architecture-decision-record — adr
URL: https://raw.githubusercontent.com/joelparkerhenderson/architecture-decision-record/main/README.md
H2: What is an architecture decision record? | How to start using ADRs | How to start using ADRs with tools | How to start using ADRs with git | Claude Code skills for ADRs | File name conventions for ADRs | Suggestions for writing good ADRs | ADR example templates | Teamwork advice for ADRs | Teamwork questions for ADRs | Next step concepts for ADRs | Architecture diagrams & views & viewpoints | Fitness functions for decisions as code | Decision guardrails for pull requests | For more information
H3: Who can create an ADR? | What justifies raising an ADR? | What justifies not raising an ADR? | What is the lifecycle of an ADR? | What are criteria for lifecycle steps of an ADR? | What roles and responsibilities interact with an ADR?

## mitodl/ol-infrastructure — adr
URL: https://raw.githubusercontent.com/mitodl/ol-infrastructure/main/docs/adr/0001-use-adr-for-architecture-decisions.md
H2: Context | Decision | Consequences | Implementation Notes | Related Decisions | References | Notes
H3: Current Situation | Problem Statement | Business/Technical Drivers | Constraints | Assumptions | Implementation Details

## app-sre/qontract-reconcile — adr
URL: https://raw.githubusercontent.com/app-sre/qontract-reconcile/master/docs/adr/ADR-001-use-adrs-for-architecture-decisions.md
H2: Context | Decision | Alternatives Considered | Consequences | Implementation Guidelines | References | Notes
H3: Difference Between ADRs and Design Documents | What Qualifies as "Significant" | What Does NOT Need an ADR | ADR Process | Alternative 1: No Formal Documentation | Alternative 2: Detailed Design Documents

## zoom/skills — runbook
URL: https://raw.githubusercontent.com/zoom/skills/main/RUNBOOK.md
H2: Skill Doc Standard Note | 1) Confirm Integration Surface | 2) Confirm Required Credentials | 3) Confirm Lifecycle Order | 4) Confirm Event/State Handling | 5) Confirm Cleanup + Upgrade Posture | 6) Quick Probes | 7) Fast Decision Tree | 8) Source Checkpoints
H3: Official docs | Raw docs in repo

## browser-use/cdp-use — runbook
URL: https://raw.githubusercontent.com/browser-use/cdp-use/main/RUNBOOK.md
H2: Releasing | Release authentication
H3: (none)

## i-dot-ai/consult — runbook
URL: https://raw.githubusercontent.com/i-dot-ai/consult/main/RUNBOOK.md
H2: Alerts | Escalation
H3: RDS

## FAILED
- https://raw.githubusercontent.com/kubernetes/kubernetes/master/SECURITY.md (404 Not Found)
- https://raw.githubusercontent.com/denoland/deno/main/SECURITY.md (404 Not Found)
- https://raw.githubusercontent.com/rust-lang/rust/master/.github/SECURITY.md (404 Not Found)
- https://raw.githubusercontent.com/hashicorp/terraform/main/.github/SECURITY.md (404 Not Found)
- https://raw.githubusercontent.com/vitejs/vite/main/.github/contributing.md (404 Not Found)
- https://raw.githubusercontent.com/denoland/deno/main/CONTRIBUTING.md (404 Not Found — Deno has no root CONTRIBUTING.md)
- https://raw.githubusercontent.com/jqlang/jq/master/CONTRIBUTING.md (404 Not Found)
- https://raw.githubusercontent.com/backstage/backstage/master/docs/architecture-decisions/README.md (404 Not Found — path moved/renamed)
- https://raw.githubusercontent.com/backstage/backstage/master/docs/architecture-decisions/adr001-github-actions.md (404 Not Found — path moved/renamed)
## Stripe — api-reference
URL: https://docs.stripe.com/api/charges/object
H2: Start here: Integrate with Stripe using skills and plugins | Attributes
H3: The Charge object

## GitHub REST API — api-reference
URL: https://docs.github.com/en/rest/issues/issues
H2: REST API endpoints for issues | List issues assigned to the authenticated user | List organization issues assigned to the authenticated user | List repository issues | Create an issue | Get an issue | Update an issue | Lock an issue | Unlock an issue | List issue suggestions | Approve an issue suggestion | Dismiss an issue suggestion | List user account issues assigned to the authenticated user
H3: Parameters | Headers | Path and query parameters | HTTP response status codes | Code examples | Example

## Node.js — api-reference
URL: https://nodejs.org/api/fs.html
H2: File system | Promise example | Callback example | Synchronous example | Promises API | Class: FileHandle | Event: 'close' | filehandle.appendFile(data[, options]) | filehandle.chmod(mode) | filehandle.chown(uid, gid) | filehandle.close() | filehandle.createReadStream([options]) | filehandle.createWriteStream([options]) | filehandle.datasync() | filehandle.fd | ... (313 total H2s, one per API member; see fsPromises.*, fs.*Sync, Class: fs.Dir, Class: fs.Dirent, Class: fs.FSWatcher, Class: fs.Stats, Class: fs.StatFs, Class: fs.ReadStream/WriteStream, fs.constants, Notes)
H3: (page uses only H2s for members; no H3 level was reported)

## Python — api-reference
URL: https://docs.python.org/3/library/argparse.html
H2: argparse — Parser for command-line options, arguments and subcommands | ArgumentParser objects | The add_argument() method | The parse_args() method | Other utilities
H3: prog | usage | description | epilog | parents | formatter_class

## MDN — api-reference
URL: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map
H2: Array.prototype.map() | In this article | Try it | Syntax | Description | Examples | Specifications | Browser compatibility | See also | Help improve MDN
H3: Parameters | Return value | Mapping an array of numbers to an array of square roots | Using map to reformat objects in an array | Using parseInt() with map() | Mapped array contains undefined

## Rust std — api-reference
URL: https://doc.rust-lang.org/std/vec/struct.Vec.html
H2: Examples | Indexing | Slicing | Capacity and reallocation | Guarantees | Implementations | Methods from Deref<Target=[T]> | Trait Implementations | Auto Trait Implementations | Blanket Implementations
H3: (none reported — page structured entirely at H2 level)

## Kubernetes — troubleshooting
URL: https://kubernetes.io/docs/tasks/debug/debug-application/
H2: Troubleshooting Applications | Feedback
H3: Debug Pods | Debug Services | Debug a StatefulSet | Determine the Reason for Pod Failure | Debug Init Containers | Debug Running Pods | Get a Shell to a Running Container

## Kubernetes — troubleshooting
URL: https://kubernetes.io/docs/tasks/debug/debug-cluster/
H2: Listing your cluster | Looking at logs | Cluster failure modes | What's next
H3: Example: debugging a down/unreachable node | Control Plane nodes | Worker Nodes | Contributing causes | Specific scenarios | Mitigations

## Docker — troubleshooting
URL: https://docs.docker.com/engine/daemon/troubleshoot/
H2: Daemon | Networking | Volumes
H3: Unable to connect to the Docker daemon | Check whether Docker is running | Check which host your client is connecting to | Troubleshoot conflicts between the daemon.json and startup scripts | Configure the daemon host with systemd | Out of memory issues

## curl — faq
URL: https://curl.se/docs/faq.html
H2: Philosophy | Install | Usage | Running | libcurl | License | PHP/CURL | Development
H3: What is curl? | What is libcurl? | What is curl not? | When would you make curl do ... ? | Who makes curl? | What do you get for making curl?

## Docker Desktop — faq
URL: https://docs.docker.com/desktop/troubleshoot-and-support/faqs/general/
H2: General FAQs for Desktop
H3: Can I use Docker Desktop offline? | How do I connect to the remote Docker Engine API? | How do I connect from a container to a service on the host? | Can I pass through a USB device to a container? | How do I verify Docker Desktop is using a proxy server? | How do I run Docker Desktop without administrator privileges?

## Vue — migration
URL: https://v3-migration.vuejs.org/
H2: Vue 3 Migration Guide | Notable New Features | Breaking Changes | New Framework-level Recommendations | Migration Build
H3: (none present on this page)

## React — migration
URL: https://react.dev/blog/2024/04/25/react-19-upgrade-guide
H2: Installing | Codemods | Breaking changes | New deprecations | Notable changes | TypeScript changes | Changelog
H3: New JSX Transform is now required | Errors in render are not re-thrown | Removed deprecated React APIs | Removed: propTypes and defaultProps for functions | Removed: Legacy Context using contextTypes and getChildContext | Removed: string refs

## Django — migration
URL: https://docs.djangoproject.com/en/5.2/howto/upgrade-version/
H2: How to upgrade Django to a newer version | Required Reading | Dependencies | Resolving deprecation warnings | Installation | Testing | Deployment
H3: Tools to help with version upgrades

## Ruby on Rails — migration
URL: https://guides.rubyonrails.org/upgrading_ruby_on_rails.html
H2: Upgrading Ruby on Rails | General Advice | Upgrading from Rails 8.0 to Rails 8.1 | Upgrading from Rails 7.2 to Rails 8.0 | Upgrading from Rails 7.1 to Rails 7.2 | Upgrading from Rails 7.0 to Rails 7.1 | Upgrading from Rails 6.1 to Rails 7.0 | Upgrading from Rails 6.0 to Rails 6.1 | Upgrading from Rails 5.2 to Rails 6.0 | Upgrading from Rails 5.1 to Rails 5.2 | Upgrading from Rails 5.0 to Rails 5.1 | Upgrading from Rails 4.2 to Rails 5.0 | Upgrading from Rails 4.1 to Rails 4.2 | Upgrading from Rails 4.0 to Rails 4.1 | Upgrading from Rails 3.2 to Rails 4.0 | Upgrading from Rails 3.1 to Rails 3.2 | Upgrading from Rails 3.0 to Rails 3.1
H3: Test Coverage | Ruby Versions | The Upgrade Process | Moving between versions | The Update Task | Configure Framework Defaults

## Terraform — migration
URL: https://developer.hashicorp.com/terraform/language/upgrade-guides
H2: Upgrading to Terraform v1.16
H3: (none present — page is largely navigation/version-selector; minimal heading content)

## Django — security
URL: https://docs.djangoproject.com/en/5.2/topics/security/
H2: Security in Django | Always sanitize user input | Cross site scripting (XSS) protection | Cross site request forgery (CSRF) protection | SQL injection protection | Clickjacking protection | SSL/HTTPS | Host header validation | Referrer policy | Cross-origin opener policy | Session security | User-uploaded content | Additional security topics
H3: (none — page contains only H2 headings)

## Ruby on Rails — security
URL: https://guides.rubyonrails.org/security.html
H2: Introduction | Authentication | Sessions | Cross-Site Request Forgery (CSRF) | Redirection and Files | User Management | Injection | Unsafe Query Generation | HTTP Security Headers | Intranet and Admin Security | Environmental Security | Dependency Management and CVEs | Additional Resources
H3: Reset Password | Implementation Details | What are Sessions? | Session Hijacking | Session Storage | Rotating Encrypted and Signed Cookies Configurations

## Google Cloud — security
URL: https://docs.cloud.google.com/docs/authentication
H2: Introduction | How to get help with authentication | Choose the right authentication method for your use case | Authorization methods for Google Cloud services | Application Default Credentials | Terminology | What's next
H3: Authentication | Authorization | Credentials | Principal | User accounts | Service accounts

## git — cli-reference
URL: https://git-scm.com/docs/git-rebase
H2: NAME | SYNOPSIS | DESCRIPTION | TRANSPLANTING A TOPIC BRANCH WITH --ONTO | MODE OPTIONS | OPTIONS | INCOMPATIBLE OPTIONS | BEHAVIORAL DIFFERENCES | MERGE STRATEGIES | NOTES | INTERACTIVE MODE | SPLITTING COMMITS | RECOVERING FROM UPSTREAM REBASE | REBASING MERGES | CONFIGURATION | GIT
H3: Empty commits | Directory rename detection | Context | Labelling of conflicts markers | Hooks | Interruptability

## AWS CLI — cli-reference
URL: https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html
H2: Description | Synopsis | Options | Global Options | Examples
H3: Note | Warning

## FAILED
- URL: https://docs.npmjs.com/faq — reason: 404 Not Found (page does not exist at this path; no dedicated npm FAQ page could be located via the docs.npmjs.com nav)
- URL: https://v2.vuejs.org/v2/guide/migration-vue-2.html — reason: 404 Not Found; replaced with the current Vue 3 migration guide (https://v3-migration.vuejs.org/) above
- URL: https://docs.stripe.com/api/charges/object — note: page's headings are mostly a flat "Attributes" bullet list rather than H2/H3 attribute subheadings; recorded as-is, not padded
- URL: https://cloud.google.com/sdk/gcloud/reference/compute/instances/create (redirects to https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) — reason: page has no semantic H2/H3 headings; content is nav-list/reference-table structured only, so no heading data could be recorded
## Ruby リファレンスマニュアル — README/インデックス
URL: https://docs.ruby-lang.org/ja/latest/doc/index.html
H2: 使用上の注意 | 目次
H3: Ruby 言語仕様 | ライブラリ | C API | その他

## Vue.js — ガイド
URL: https://ja.vuejs.org/guide/introduction.html
H2: Vue とは？ | プログレッシブフレームワーク | 単一ファイルコンポーネント | 2 つの API スタイル | さらに知りたいことはありますか？ | 学習方法を選びましょう
H3: Options API | Composition API | どちらを選ぶか？

## React — チュートリアル (クイックスタート)
URL: https://ja.react.dev/learn
H2: コンポーネントの作成とネスト | JSX でマークアップを書く | スタイルの追加 | データの表示 | 条件付きレンダー | リストのレンダー | イベントに応答する | 画面の更新 | フックの使用 | コンポーネント間でデータを共有する | 次のステップ
H3: (なし。H2 のみで構成)

## MDN Web Docs — リファレンス
URL: https://developer.mozilla.org/ja/docs/Web/HTML
H2: HTML: ハイパーテキストマークアップ言語 | 目次 | 初心者向けチュートリアル | ガイド | 手引き | リファレンス | 関連トピック | MDN の改良に協力
H3: 要素別の属性 | 属性値 | HTML guides | HTML reference | CSS reference | Web API reference

## Python — チュートリアル
URL: https://docs.python.org/ja/3/tutorial/introduction.html
H2: 3. 形式ばらない Python の紹介 | 3.1. Python を電卓として使う | 3.1.1. 数 | 3.1.2. テキスト | 3.1.3. リスト型 (list) | 3.2. プログラミングへの第一歩
H3: 前のトピックへ | 次のトピックへ | This page | ナビゲーション

## Django — チュートリアル
URL: https://docs.djangoproject.com/ja/5.1/intro/tutorial01/
H2: はじめての Django アプリ作成、その 1 | プロジェクトを作成する | 開発用サーバー | Polls アプリケーションをつくる | はじめてのビュー作成
H3: プロジェクトとアプリケーション | runserver の自動リロード | include() を使うとき | ページが見つかりませんか？ | Support Django! | 助けを求める

## Ruby on Rails ガイド — getting-started (チュートリアル)
URL: https://railsguides.jp/getting_started.html
H2: はじめに | Railsとは何か | Railsアプリを新規作成する | Hello, Rails! | データベースモデルを作成する | Railsコンソール | Active Recordモデルの基礎 | Railsのリクエストの流れ | ルーティング | コントローラとアクション | 認証機能を追加する | 製品をキャッシュに乗せる | フィールドをAction Textでリッチテキストにする | Active Storageでファイルアップロード機能を追加する | 国際化（I18n） | Action Mailerとメール通知 | CSSとJavaScriptを追加する | Railsでテストを書く | RuboCopでコードの形式を統一する | セキュリティチェック | GitHub ActionsでCIを実行する | Kamalでproduction環境にデプロイする
H3: MVCの基礎 | 開発中の自動コード読み込み | データベースのマイグレーション | レコードを作成する | CRUDアクション | before_actionコールバックでコードをDRYにする

## Kubernetes — インストール手順
URL: https://kubernetes.io/ja/docs/tasks/tools/install-kubectl-linux/
H2: 始める前に | Linuxへkubectlをインストールする | kubectlの設定を検証する | オプションのkubectlの設定とプラグイン | 次の項目
H3: curlを使用してLinuxへkubectlのバイナリをインストールする | ネイティブなパッケージマネージャーを使用してインストールする | 他のパッケージマネージャーを使用してインストールする | シェルの自動補完を有効にする | kubercを設定する | kubectl convertプラグインをインストールする

## TypeScript Deep Dive (typescriptbook.jp) — ガイド
URL: https://typescriptbook.jp/overview
H2: TypeScriptのあらまし
H3: TypeScriptの特徴 | JavaScriptはTypeScriptの一部 | TypeScript誕生の背景 | TypeScriptとエコシステム | なぜTypeScriptを使うべきか | 静的型付け

## Laravel 日本語ドキュメント — インストール
URL: https://readouble.com/laravel/11.x/ja/installation.html
H2: Laravelとの出会い | Laravelアプリの生成 | 初期設定 | Herd使用のローカルインストール | Sailで使用するDockerのインストール | IDEサポート | 次のステップ
H3: なぜLaravelなのか？ | PHPとLaravelインストーラのインストール | アプリケーションの生成 | 環境ベースの設定 | データベースとマイグレーション | ディレクトリ設定

## GitHub Docs — チュートリアル (Hello World)
URL: https://docs.github.com/ja/get-started/quickstart/hello-world
H2: はじめに | 手順 1: リポジトリを作成する | 手順 2: ブランチを作成する | 手順 3: 変更を行いコミットする | 手順 4: Pull request を開く | 手順 5: pull request をマージする | Conclusion | 次のステップ | 詳細については、次を参照してください。
H3: 前提条件 | ブランチの作成 | プルリクエストのレビュー

## Vite — ガイド
URL: https://ja.vite.dev/guide/
H2: 概要 | ブラウザー対応 | Vite をオンラインで試す | 最初の Vite プロジェクトを生成する | コミュニティーのテンプレート | 手動インストール | index.html とプロジェクトルート | コマンドラインインターフェイス | 未リリースのコミットの使用 | コミュニティー
H3: 代替ルートの指定 | 代わりに、ローカルマシンに vite repo をクローンしてから自分でビルドとリンクをすることもできます

## Mackerel — getting-started (チュートリアル)
URL: https://mackerel.io/ja/docs/entry/getting-started
H2: オーガニゼーションに所属する | 次に行うこと | 困った時は
H3: オーガニゼーションを新規作成する | 既存のオーガニゼーションに加入する | ホストを登録する | ホストを管理する | ホストを監視する | さまざまなメトリックを投稿する

## Firebase (Cloud Functions) — チュートリアル
URL: https://firebase.google.com/docs/functions/get-started?hl=ja
H2: このチュートリアルについて | Firebase プロジェクトを作成する | 環境と Firebase CLI を設定する | プロジェクトの初期化 | 必要なモジュールをインポートしてアプリを初期化する | メッセージを追加する関数の追加 | 大文字に変換する関数の追加 | 関数の実行をエミュレートする | 本番環境に関数をデプロイする | 次のステップ
H3: Firebase または Google Cloud を初めて使用する | 既存の Google Cloud プロジェクト | Node.js | Python

## Spring (spring.pleiades.io 日本語翻訳) — チュートリアル
URL: https://spring.pleiades.io/guides/gs/rest-service/
H2: 構築するもの | 必要なもの | 本ガイドの完成までの流れ | Spring Initializr から開始 | リソース表現クラスを作成する | リソースコントローラーを作成する | サービスを実行する | サービスをテストする | 要約 | 関連事項 | コードを入手する | クラウドでの作業 | プロジェクト
H3: 実行可能 JAR を構築する

## PHP マニュアル — チュートリアル
URL: https://www.php.net/manual/ja/tutorial.php
H2: 簡易チュートリアル | 目次
H3: Found A Problem? | User Contributed Notes

## LINE Developers (Messaging API) — getting-started
URL: https://developers.line.biz/ja/docs/messaging-api/getting-started/
H2: Messaging APIを始めよう | チャネルとは | 1. LINE公式アカウントを作成する | 2. LINE公式アカウントでMessaging APIを有効にする | 【廃止】LINE Developersコンソールでチャネルを作成する | 次のステップ
H3: 1-1. ビジネスIDに登録する | 1-2. 作成フォームに必要事項を記入する | 1-3. LINE公式アカウントを確認する | 2-1. Messaging APIの利用を有効にする | 2-2. LINE Developersコンソールにログインする | 2-3. チャネルを確認する

## freee Developers Community — チュートリアル
URL: https://developer.freee.co.jp/tutorials
H2: (このページに H2 見出しは無い)
H3: freee APIを活用したアプリケーションを実装する | freee APIをブラウザから試してみる | freee APIスタートガイド | アプリケーションを作成する | アクセストークンを取得する | 最初のGET/POSTリクエストを行う

## FAILED

- https://raw.githubusercontent.com/yamadashy/repomix/main/README.ja.md — HTTP 404 (このパスに日本語版 README は存在しない。README.md 直下に日本語版があるか未確認、再調査が必要)
- https://git-scm.com/book/ja/v2/使い始める-Gitとは — HTTP 404 (URL エンコードした日本語見出しパスが実サイトの slug と一致しない)
- https://developer.mozilla.org/ja/docs/Learn_web_development/Getting_started/Your_first_website/Installing_basic_software — HTTP 404 (MDN 側でページ構成が変更/移動済みの可能性)
- https://misskey-hub.net/docs/for-developers/api/get-started/ — HTTP 404
- https://misskey-hub.net/docs/for-developers/api/get-started.html — HTTP 404
- https://misskey-hub.net/docs/for-developers/api/ — HTTP 404 (WebSearch 結果は /en/docs/... のみ返し、日本語版パスの構造が特定できなかった)
- https://nginx.org/ja/docs/beginners_guide.html — 取得はできたが本文が英語のまま（/ja/ パスでも日本語訳が提供されておらず、対象外として除外）
- サイボウズ 開発ハンドブック (github) — 該当する実在リポジトリを WebSearch で特定できず、URL 未確定のため取得断念
- Mercari engineering handbook (日本語 README) — WebSearch で該当する具体的な日本語ドキュメントファイルを特定できず、取得断念
- misskey-dev/misskey CONTRIBUTING.md — 取得は成功したが英語主体で日本語セクションは一部（その他/考え方など）のみのため、「日本語で書かれたドキュメント」の対象から除外（データとして採用せず）
## Ruby on Rails (railsguides.jp) — チュートリアル
URL: https://railsguides.jp/getting_started.html
H2: Rails をはじめよう | はじめに | Railsとは何か | Railsアプリを新規作成する | ディレクトリ構造 | MVCの基礎 | Hello, Rails! | 開発中の自動コード読み込み | データベースモデルを作成する | データベースのマイグレーション | マイグレーションを実行する | Railsコンソール | Active Recordモデルの基礎 | レコードを作成する | レコードをクエリで取り出す | レコードのフィルタリングと並べ替え | レコードを検索する | レコードを更新する | レコードを削除する | バリデーション | Railsのリクエストの流れ | ルーティング | URLの構成要素 | HTTPメソッドとその目的 | Railsのルーティング | ルーティングコマンド | コントローラとアクション | リクエストを作成する | インスタンス変数 | CRUDアクション | 個別の製品を表示する | 製品を作成する | 製品を編集する | 製品を削除する | 認証機能を追加する | ログアウト機能を追加する | 認証なしのアクセスも許可する | 認証済みユーザーにだけリンクを表示する | 製品をキャッシュに乗せる | フィールドをAction Textでリッチテキストにする | Active Storageでファイルアップロード機能を追加する | 国際化（I18n） | Action Mailerとメール通知 | 基本的な在庫トラッキング機能 | 通知の購読者を製品に追加する | 「在庫あり」メールによる通知機能を追加する | 共通コードをconcernに抽出する | 通知購読の解除リンクをメールに追加する | CSSとJavaScriptを追加する | Propshaft | importmap | Hotwire | Railsでテストを書く | フィクスチャ | メール送信をテストする | RuboCopでコードの形式を統一する | セキュリティチェック | GitHub ActionsでCIを実行する | Kamalでproduction環境にデプロイする | production環境でユーザーを作成する | Solid Queueでバックグラウンドジョブを処理する | 今後のステップ | 関連リンク
H3: CRUDのルーティング | Strong Parameters | ビューをパーシャルに切り出す | before_actionコールバックでコードをDRYにする | Notifications モジュール | フィクスチャ

## Ruby on Rails (railsguides.jp) — セキュリティガイド
URL: https://railsguides.jp/security.html
H2: はじめに | 認証機能 | セッション | クロスサイトリクエストフォージェリ（CSRF） | リダイレクトとファイル | ユーザー管理 | インジェクション | 安全でないクエリ生成 | HTTPセキュリティヘッダー | イントラネットとAdminのセキュリティ | 利用環境のセキュリティ | 依存関係の管理とCVEについて | 追加資料 | 関連リンク
H3: パスワードをリセットする | セッション固定攻撃 - 対応策 | クロスサイトスクリプティング（XSS） | SQLインジェクション | Content-Security-Policy ヘッダー | 独自のcredential

## Laravel (readouble.com 11.x) — インストール
URL: https://readouble.com/laravel/11.x/ja/installation.html
H2: Laravelとの出会い（Meet Laravel） | Laravelアプリの生成（Creating a Laravel Application） | 初期設定（Initial Configuration） | Herd使用のローカルインストール（Local Installation Using Herd） | Sailで使用するDockerのインストール（Docker Installation Using Sail） | IDEサポート（IDE Support） | 次のステップ（Next Steps）
H3: なぜLaravelなのか？（Why Laravel?） | PHPとLaravelインストーラのインストール（Installing PHP and the Laravel Installer） | アプリケーションの生成（Creating an Application） | 環境ベースの設定（Environment Based Configuration） | データベースとマイグレーション（Databases and Migrations） | macOSでのHerd（Herd on macOS）

## Laravel (readouble.com 11.x) — ガイド (キュー)
URL: https://readouble.com/laravel/11.x/ja/queues.html
H2: イントロダクション | ジョブの生成 | ジョブミドルウェア | ジョブのディスパッチ | 最大試行回数／タイムアウト値の指定 | エラー処理 | ジョブバッチ | クロージャのキュー投入 | キューワーカの実行 | 失敗したジョブの処理 | Supervisorの設定
H3: 接続 対 キュー | 一意なジョブ | レート制限 | ジョブのオーバーラップの防止 | バッチへのジョブ追加 | DynamoDB設定

## Docker (docs.docker.jp) — 設定 (リソース制約)
URL: https://docs.docker.jp/config/containers/resource_constraints.html
H2: メモリ、CPU、GPU に対する実行時オプション | メモリ | CPU | GPU
H3: メモリ不足時のリスクへの理解 | コンテナーに対するメモリアクセスの制限 | --memory-swap の詳細 | デフォルト CFS スケジューラの設定 | リアルタイム・スケジューラの設定 | NVIDIA GPU へのアクセス

## Docker (docs.docker.jp) — チュートリアル (swarmモード)
URL: https://docs.docker.jp/engine/swarm/swarm-tutorial/index.html
H2: swarm モード導入ガイド | セットアップ | 接続した3台のマシン | manager マシンの IP アドレス | ホスト間で開くプロトコルとポート | 次は何をしますか？
H3: Linux マシン上に Docker Engine をインストール | Docker Desktop for mac か Docker Desktop for Windows を使う | three-networked-host-machine | swarm-tutorial-setup | open-protocols-and-ports-between-the-hosts | manager-ip

## Docker (docs.docker.jp) — 設定 (ボリューム)
URL: https://docs.docker.jp/storage/volumes.html
H2: ボリュームの使用 | -v と --mount フラグの選択 | -v と --mount との挙動の違い | ボリュームの作成と管理 | ボリュームを使ってコンテナを起動 | docker-compose でボリュームを使う | マシン間のデータ共有 | ボリュームドライバをの使用 | データボリュームのバックアップ、復旧、移行 | ボリューム削除 | 次のステップ
H3: サービスに対する構文の違い | 初期セットアップ | ボリュームドライバを使ってボリュームを作成 | CIFS/Samba ボリュームの作成 | ボリュームのバックアップ | 無名ボリューム(anonymous volume) の削除

## Docker Compose (docs.docker.jp) — APIリファレンス (Compose Specification)
URL: https://docs.docker.jp/compose/compose-file/index.html
H2: Compose Specification（仕様） | この文章の状態 | 動作条件とオプションの属性 | Compose のアプリケーション モデル | 説明例 | Compose ファイル | version トップレベル要素 | name トップレベル要素 | services トップレベル要素 | networks トップレベル 要素(element) | volumes トップレベル 要素(element) | configs トップレベル 要素(element) | secrets トップレベル 要素(element) | フラグメント(fragment) | 拡張(extension) | 変数展開（補完） | Compose のドキュメント
H3: profiles | blkio_config | depends_on | networks | ports | volumes

## Kubernetes 日本語 (kubernetes.io/ja) — トラブルシューティング (Podのデバッグ)
URL: https://kubernetes.io/ja/docs/tasks/debug/debug-application/debug-pods/
H2: Podのデバッグ | 問題の診断 | 次の項目 | フィードバック
H3: Podのデバッグ | レプリケーションコントローラーのデバッグ | Serviceのデバッグ | PodがPendingのまま | Podがwaitingのまま | Podがクラッシュするなどの不健全な状態

## Kubernetes 日本語 (kubernetes.io/ja) — 概念 (Pod)
URL: https://kubernetes.io/ja/docs/concepts/workloads/pods/
H2: Podとは何か？ | Podを使用する | Podを利用する | Podの更新と取替 | リソースの共有と通信 | コンテナの特権モード | static Pod | コンテナのProbe | 次の項目
H3: Podを管理するためのワークロードリソース | Podが複数のコンテナを管理する方法 | Pod OS | Podとコンテナコントローラー | Podテンプレート | Pod内のストレージ / Podネットワーク

## Kubernetes 日本語 (kubernetes.io/ja) — トラブルシューティング (DNS解決のデバッグ)
URL: https://kubernetes.io/ja/docs/tasks/administer-cluster/dns-debugging-resolution/
H2: 始める前に | 既知の問題 | 次の項目
H3: テスト環境として使用するシンプルなPodを作成する | まずはローカルのDNS設定を確認する | DNSのPodが実行されているか確認する | DNSのPodのエラーを確認する | DNSサービスは起動しているか | DNSエンドポイントは公開されているか

## Git (git-scm.com/book/ja) — ガイド (サブモジュール)
URL: https://git-scm.com/book/ja/v2/Git-のさまざまなツール-サブモジュール
H2: サブモジュール | サブモジュールの作り方 | サブモジュールを含むプロジェクトのクローン | サブモジュールを含むプロジェクトでの作業 | サブモジュールのヒント | サブモジュール使用時に気をつけるべきこと
H3: 上流の変更の取り込み | サブモジュールでの作業 | サブモジュールに加えた変更の公開 | 変更されたサブモジュールのマージ | Submodule Foreach | 便利なエイリアス

## Django 日本語 (docs.djangoproject.com/ja) — インストール
URL: https://docs.djangoproject.com/ja/5.1/topics/install/
H2: Django のインストール方法 | Python をインストールする | Apache と mod_wsgi のインストール | データベースを動かす | Django コードをインストールする
H3: pip を使用して公式リリースをインストールする | 特定ディストリビューション向けのパッケージをインストールする | 開発バージョンをインストールする

## Redmine (redmine.jp) — インストール
URL: https://redmine.jp/tech_note/install/
H2: Redmineのインストール | インストール作業 | とりあえずの設定 | Apacheとの連携 | 調べる | 試す | 関連サイト | メールマガジン
H3: Redmineのダウンロードおよびインストール | データベース接続設定(config/database.yml) | セッション暗号化用鍵の生成 | データベースの初期化 | メール送信設定(config/email.yml) | Redmineの起動

## Groonga (groonga.org/ja) — インストール
URL: https://groonga.org/ja/docs/install.html
H2: 2. インストール
H3: 2.1. Windows | 2.2. macOS | 2.3. Debian GNU/Linux | 2.4. Ubuntu | 2.5. AlmaLinux | 2.6. Amazon Linux

## PHP 日本語マニュアル (php.net/manual/ja) — セキュリティ
URL: https://www.php.net/manual/ja/security.php
H2: セキュリティ
H3: はじめに | 一般的な考慮事項 | CGI バイナリとしてインストール | Apache モジュールとしてインストール | セッションのセキュリティ | ファイルシステムのセキュリティ

## Vue.js 日本語 (ja.vuejs.org) — ガイド (テスト)
URL: https://ja.vuejs.org/guide/scaling-up/testing.html
H2: なぜテストをするのか？ | いつテストをするか？ | テストの種類 | 概要 | 単体テスト | コンポーネントのテスト | E2E テスト | レシピ
H3: コンポーザブル | コンポーネントの単体テスト | 推奨事項 | マウントするライブラリー | E2E テストソリューションの選択 | クロスブラウザーテスト

## WordPress 日本語 (ja.wordpress.org) — FAQ (インストール)
URL: https://ja.wordpress.org/support/article/faq-installation/
H2: カテゴリー | 翻訳・改善にご協力ください | FAQ/インストール | インストール | 高度なインストール | FTP | MySQL もしくは MariaDB | PHP | インポート | この記事は役に立ちましたか ? どうすればさらに改善できますか ?
H3: WordPress のインストール方法は ? | WordPress に適したホストを見つけるにはどうすればよいですか ? | wp-config.phpファイルを設定するにはどうすればよいですか ? | データベースの作成は必要ですか ? | Webサイトに 403 エラーが表示されるのはなぜですか ? | 別のディレクトリにあるファイルを使用して、WordPress をインストールするにはどうすればよいですか ?

## FAILED
- https://git-scm.com/book/ja/v2/Git-のさまざまなツール-トラブルシューティング — HTTP 404（スラッグ不正、代替として「サブモジュール」ページを収集）
- https://www.zabbix.com/documentation/current/ja/manual/installation/install — HTTP 404
- https://www.zabbix.com/documentation/current/ja/manual/installation — HTTP 404（日本語版インストールページのURLパス特定できず）
- https://docs.fluentd.org/v/1.0/quickstart — HTTP 404。加えて公式情報として docs.fluentd.org からは日本語ドキュメントが削除済み（Qiita記事で確認）、現行版に日本語クイックスタートは存在しない
- https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html — 日本語版が存在しない（英語のみ、日本語版リンクなし）
- https://www.postgresql.jp/document/16/html/backup.html — 取得成功したがH2見出しが存在せず（目次のみのページ構造）、見出しリストとして採用不可
- https://dev.mysql.com/doc/refman/8.0/ja/replication.html — 取得成功したがH2見出しが存在せず（目次のみのページ構造）、見出しリストとして採用不可
- https://docs.gitlab.com/ee/topics/git/troubleshooting_git.html — 日本語版が存在しない（英語のみ）

## MDN Web Docs 日本語 — ガイド (HTTP キャッシュ)
URL: https://developer.mozilla.org/ja/docs/Web/HTTP/Guides/Caching
H2: HTTP キャッシュ | 目次 | キャッシュの種類 | ヒューリスティックキャッシュ | age に基づく新鮮さと古さ | 有効期限または max-age | Vary | 検証 | キャッシュしない | 再読み込みと強制再読み込み | 格納されたレスポンスの削除 | リクエストの折りたたみ | 良くあるキャッシュパターン | 関連情報 | MDN の改良に協力
H3: プライベートキャッシュ | 共有キャッシュ | プロキシーキャッシュ | マネージドキャッシュ | 強制的な再検証 | 既定の設定

## React 日本語 — 概念解説 (レンダーとコミット)
URL: https://ja.react.dev/learn/render-and-commit
H2: ステップ 1：レンダーのトリガ | ステップ 2：React がコンポーネントをレンダー | ステップ 3：React が DOM への変更をコミットする | エピローグ：ブラウザのペイント
H3: 初回レンダー | state 更新後の再レンダー | パフォーマンスの最適化

## Kubernetes 日本語 — 概念 (Service)
URL: https://kubernetes.io/ja/docs/concepts/services-networking/service/
H2: KubernetesにおけるService | Serviceの定義方法 | Serviceタイプ | ヘッドレスService | Serviceの検出 | 仮想IPアドレッシング機構 | 外部IP | APIオブジェクト
H3: クラウドネイティブなサービスディスカバリ | ポート定義 | セレクター無しのService | `type: ClusterIP` | 環境変数 | スティッキーセッション
