# Archive

Retired drafts, design variations and Figma capture files, moved out of the working tree so they
stop showing up in searches. Paths mirror where each folder used to live.

**Nothing in here is current.** It is not precedent, not a component source, and not an example to
copy from. It is kept only so the history of a design decision can be recovered if someone asks
"why did we stop doing it that way".

If you are an agent: don't read these unless you were explicitly asked about an archived file
by name.

## `japanese-beginner/`

A different product — teaching **Japanese**, where everything else here teaches Korean to
Japanese speakers. Active Feb–Apr 2026, retired Aug 2026. It never moved to
`podo-curriculum`, which is Korean-only, so nothing downstream reads it.

It was also the only consumer of the repo's hand-rolled live-sync server — a WebSocket
relay (`sync-server.js`, plus `package.json`, `package-lock.json` and a `Dockerfile` to
run it) that mirrored tutor and learner screens. Korean decks get that from lemonboard's
`data-sync` contract instead, so the server was deleted rather than archived with the
lessons. The archived lesson pages still contain their client code; it auto-detects a
WebSocket URL from the current host and simply does nothing when none answers, so they
open and read fine — they just no longer sync.
