# podo-curriculum-public — archived

**The curriculum is no longer written here.** Authoring moved to
[`re-speak/podo-curriculum`](https://github.com/re-speak/podo-curriculum) on
2026-08-19, which is now the only place lessons are written *and* the place they
deploy from.

This repository is kept for one reason: the licensed textbook scans in
`korean/references/curricula/`. They are 726MB of private source material, one
file past GitHub's 100MB ceiling, and nothing in any build reads them. Everything
derived from them — the pattern maps, the clean text, the wireframes — came
across and lives at `references/kr/` there.

## Where things went

| here | there |
|---|---|
| `runtime/{css,js}` | `shared/{css,js}` — now the source, published to the CDN by tag |
| `korean/tracks/`, `korean/trial/` | `sandbox/drafts/kr/` |
| `english/tracks/` | `sandbox/drafts/en/` |
| `english/reference/` | `sandbox/drafts/en/reference/` |
| `korean/tools/` (29 scripts) | `tools/authoring/kr/` |
| `english/tools/` (25 scripts) | `tools/authoring/en/` |
| `korean/references/{curricula,reports}` | `references/kr/` — minus the licensed PDFs, which stayed |
| `AGENTS.md`, `CLAUDE.md`, the workflow and blueprint docs | alongside their language under `sandbox/drafts/<code>/` |

`ux-philosophy.md` is at `shared/ux-philosophy.md` there, and is still the
contract for every lesson page.

## Do not edit anything here

There is no sync any more. The tool that used to mirror this repository into
`podo-curriculum` was deleted rather than deprecated, because a script that
replaces the authoring tree wholesale is not something to leave lying around once
the tree it would overwrite is the original.

So an edit made here reaches nobody, and — worse — leaves two files that disagree
with no signal about which one a learner is looking at. Make the change in
`re-speak/podo-curriculum` instead.

The GitHub Pages site built from this repository is likewise frozen. The public
catalog is built from `courses/` in the new repository, which is what actually
deploys, so the page and the class cannot disagree.
