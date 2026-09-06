# Worker status protocol

This session runs supervisor plus workers. A worker owns one task, works on its own branch
`work/<task>`, and has no back-channel to the supervisor. It communicates by committing
`.agents/<task>/STATUS.md` on its branch, on every meaningful change.

```
status: running | blocked | done | failed
updated: <UTC timestamp, e.g. 2026-09-06T14:12:00Z>
done:
  - what is finished
next:
  - the immediate next step
questions:
  - a question concrete enough that research can answer it
needs_owner:
  - only what genuinely only the repository owner can decide
```

The supervisor reads these with `git fetch` and a look at each branch. It answers
`questions` itself from research where it can, restarts a worker whose `updated` is older
than sixty minutes while `status: running`, and bundles `needs_owner` for the owner with a
recommendation per line.

No branch merges to the integration branch without the owner's go.
