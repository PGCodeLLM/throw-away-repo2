---
name: dictation
description: Dictation instructions for cleaning up speech-to-text transcripts in the gh-aw (GitHub Agentic Workflows) project. Fixes misrecognized technical terms, spacing, and hyphenation, and removes filler words to make dictated text clear and professional.
---

# Dictation Instructions

## Technical Context

gh-aw (GitHub Agentic Workflows) lets you author AI-driven workflows as markdown files with YAML frontmatter, which compile to GitHub Actions lockfiles (`.lock.yml`). Workflows declare an engine (claude, codex, copilot, custom), tools (bash, edit, github, playwright, web-fetch, web-search), permissions, and safe-outputs (such as create-pull-request) that run inside a sandbox with MCP servers. When dictating about this project, expect frequent references to these configuration keys, engine names, tool types, and `GH_AW_*` environment variables.

## Project Glossary

These are the project-specific terms that appear in this codebase. When a dictated word closely matches one of these (allowing for speech-to-text errors), prefer the exact spelling, casing, spacing, and hyphenation shown here.

.lock.yml
@copilot
activation
add-comment
add_comment
agent
agent-stdio.log
agent_output
agent_output.json
agentic workflow
agentic workflows
agentics
agentify
agentifying
agents
AGENTS.md
ambiguous
ANTHROPIC_API_KEY
ANTHROPIC_BASE_URL
antigravity
api.anthropic.com
artifact
audit
auto-merge
aw-prompts
aw_context
bash
branch
cache-memory
capitalization
checkout
clarity
claude
Claude Code
CLAUDE.md
cleanup
client_payload
codex
comment_id
compile
concurrency
config.json
contents
context
continue-on-error
copilot
core
create-issue
create-pull-request
create_issue
create_pull_request
crush
custom
default_branch
defaults
dictation
dictation-prompt
DICTATION.md
discussion
discussions
docker.sock
DOCKER_HOST
DOCKER_SOCK_PATH
download-artifact
draft
edit
engine
event
exec
expires
fetch
fetch-depth
filler words
fmt
folders
frequency histogram
fromJSON
frontmatter
gateway
gemini
getOctokit
gh-aw
GH_AW_AGENT_OUTPUT
GH_AW_CI_TRIGGER_TOKEN
GH_AW_CURRENT_WORKFLOW_REF
GH_AW_ENGINE_ID
GH_AW_GITHUB_ACTOR
GH_AW_GITHUB_MCP_SERVER_TOKEN
GH_AW_GITHUB_REPOSITORY
GH_AW_GITHUB_RUN_ID
GH_AW_GITHUB_TOKEN
GH_AW_GITHUB_WORKSPACE
GH_AW_INFO_BODY_MODIFIED
GH_AW_INFO_ENGINE_ID
GH_AW_INFO_VERSION
GH_AW_MCP_LOG_DIR
GH_AW_MODEL_AGENT_CLAUDE
GH_AW_NODE_EXEC
GH_AW_PROMPT
GH_AW_SAFE_OUTPUTS
GH_AW_SAFE_OUTPUTS_API_KEY
GH_AW_SAFE_OUTPUTS_CONFIG_PATH
GH_AW_SAFE_OUTPUTS_PORT
GH_AW_SAFE_OUTPUTS_TOOLS_PATH
GH_AW_SETUP_WORKFLOW_NAME
GH_AW_WORKFLOW_NAME
GH_AW_WORKFLOW_SOURCE
GH_AW_WORKFLOW_SOURCE_URL
GH_HOST
ghcr.io
github
github-actions
github-mcp-server
github-script
github-token
github.actor
github.com
github.event.comment.id
github.event.discussion.number
github.event.issue.number
github.event.pull_request.number
github.event_name
github.job
github.ref
github.repository
github.run_id
github.server_url
github.token
github.workspace
GITHUB_MCP_GUARD_MIN_INTEGRITY
GITHUB_MCP_GUARD_REPOS
GITHUB_MCP_SERVER_TOKEN
GITHUB_OUTPUT
GITHUB_SERVER_URL
GITHUB_TOKEN
GITHUB_WORKSPACE
githubnext
glossary
homophone
host.docker.internal
hyphenation
if-no-files-found
imports
integrity
interim
issue
issues
item_number
item_type
labels
lint
localhost
lockfile
logs
lts-alpine
markdown
maxLength
mcp
MCP server
MCP servers
mcp-config
mcp-logs
mcp-payloads
MCP_GATEWAY_API_KEY
MCP_GATEWAY_DOMAIN
MCP_GATEWAY_PAYLOAD_DIR
MCP_GATEWAY_PORT
misrecognition
missing_data
missing_tool
model
MultiEdit
needs
needs.activation.outputs
needs.agent.outputs.output_types
needs.agent.result
network
node
noop
NOTES.md
opencode
origin
outcome
output
output_types
parent-span-id
payload
permissions
persist-credentials
playwright
poutine
professional
prompt.txt
prompts
proper noun
pull-requests
pull_request
punctuation
push-to-pull-request-branch
Read
README
recompile
ref
remote
report_incomplete
reporting.md
repository
runner.temp
RUNNER_TEMP
runs-on
runtime
safe-output
safe-outputs
safeoutputs
sandbox
sanitize
schedule
search
secrets
secrets.ANTHROPIC_API_KEY
secrets.GITHUB_TOKEN
setup
Setup Agent
setup-node
setup_globals.cjs
setupGlobals
skills
source
spacing
span
span-id
speech-to-text
steps
strict
test-unit
threat-detection
timeout-minutes
title-prefix
tokens
toolset
toolsets
trace-id
transcription
ubuntu-slim
untrusted_checkout_exec
update-issue
update_issue
upload-artifact
utterance
verbatim
vocabulary
voice
web-fetch
web-search
workflow
workflow_dispatch
workflows
workspace
Write
YAML

## Fix Speech-to-Text Errors

Correct common misrecognitions to the canonical project term:

- "G H A W" / "G-H-A-W" / "gee aitch ay double-you" / "gas" → `gh-aw`
- "agent ic" / "a gentic" / "agen tick" → agentic
- "agentic work flows" / "agent workflows" → agentic workflows
- "front matter" / "front-matter" → frontmatter
- "lock file" / "dot lock dot yml" / "lock yaml" → `.lock.yml` (lockfile)
- "safe outputs" / "safe output" → safe-outputs
- "create pull request" / "create P R" → create-pull-request
- "M C P" / "em see pee" → MCP (MCP server)
- "M C P server" / "mcp gateway" → MCP server / MCP_GATEWAY_*
- "cloud" / "clod" / "claud" → claude
- "codecs" / "co decks" / "codex's" → codex
- "co pilot" / "copilot at" → @copilot
- "yaml" / "yam-el" / "ya mil" → YAML
- "work flow dispatch" / "workflow dispatch" → workflow_dispatch
- "pull request" (as event) → pull_request
- "runs on" / "runs-on" → runs-on
- "timeout minutes" → timeout-minutes
- "cache memory" → cache-memory
- "tool set" / "tool sets" → toolset / toolsets
- "web fetch" / "web search" → web-fetch / web-search
- "play write" / "playwrite" → playwright
- "G H A W github token" / "gee aitch ay double-you token" → `GH_AW_GITHUB_TOKEN`
- "anthropic A P I key" → `ANTHROPIC_API_KEY`
- "anthropic base U R L" → `ANTHROPIC_BASE_URL`
- "runner temp" / "runner dot temp" → `RUNNER_TEMP` / runner.temp
- "git hub" / "git-hub" → github / GitHub
- "git hub script" → github-script
- "git hub actions" → github-actions
- "git hub M C P server" → github-mcp-server
- spelled-out env var names ("G H A W safe outputs") → restore underscores and uppercase (`GH_AW_SAFE_OUTPUTS`)
- collapse spaces inside identifiers and restore hyphens, dots, and underscores to match the glossary spelling

## Clean Up and Improve Text

Make dictated text read like clear, professional written English:

- Remove filler words and verbal tics: humm, um, uh, er, like, you know, I mean, sort of, kind of, basically, actually, literally, just, so yeah, right.
- Remove false starts, repeated words, and self-corrections; keep only the intended final phrasing.
- Fix run-on sentences by adding sentence boundaries and punctuation; capitalize sentence starts and proper nouns.
- Convert spoken punctuation cues ("comma", "period", "new line") into the actual punctuation when clearly intended.
- Tighten rambling phrasing into concise statements while preserving the user's intended meaning.
- Apply correct spacing, casing, and hyphenation for the project terms listed in the glossary.

## Guidelines

You do not have enough background information to plan or provide code examples.
- do NOT generate code examples
- do NOT plan steps
- focus on fixing speech-to-text errors and improving text quality
- remove filler words (humm, you know, um, uh, like, basically, actually, etc.)
- improve clarity and make text more professional
- maintain the user's intended meaning
