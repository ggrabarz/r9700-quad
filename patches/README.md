# Saber upstream patches

## `saber-4x-r9700-docs.patch`

**Target:** [GGZ14/saber-engine](https://github.com/GGZ14/saber-engine) at `cebec82` (the clone’s `HEAD` when this was prepared, 2026-11-06).
**Branch:** `4x-r9700-docs` (local).
**Contents:** docs only — no engine code.

- `docs/4X-R9700.md` — the four-card R9700 hardware envelope, what works today (one TP=2 server on a pair), what does not (TP=3/4, two servers on four cards with the current launcher), the 95.4 GiB PLE/O_DIRECT storage note and a benchmark plan.
- `docs/RFC-4-RANK.md` — design proposal for a four-rank mode: EP=4 + dense TP=2 vs pipeline/layer split, with the code touchpoints and acceptance gates.

**Why docs only:** the code change is not a config expansion. Flash-Next has 2 KV heads, so dense TP=4 would need 0.5 KV heads per rank; the current executor, all-reduce and pack are two-rank. The RFC is the right first step; a code PR without a 4-rank all-reduce and a 4-rank pack would not run.

**Apply:**

```sh
git clone https://github.com/GGZ14/saber-engine.git
cd saber-engine
git checkout -b 4x-r9700-docs cebec82
git am /path/to/saber-4x-r9700-docs.patch
```

**Submit:** there is no `gh` client on this host, so the patch is local. On a machine with `gh auth login`:

```sh
gh repo fork GGZ14/saber-engine --clone=false
git remote add fork https://github.com/<you>/saber-engine.git
git push -u fork 4x-r9700-docs
gh pr create --repo GGZ14/saber-engine --head <you>:4x-r9700-docs \
  --title "docs: add 4x R9700 host guide and 4-rank RFC" \
  --body-file /path/to/PR-BODY.md
```

A ready PR body is in `PR-BODY.md`.

**Note:** the patch is against `cebec82`. If upstream has moved, `git am -3` may be needed; the two new files are independent of existing files, so a rebase is usually trivial.
