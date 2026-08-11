# Curriculum proofreading workflow

This workflow reviews authored lesson language without feeding reviewers the runtime HTML. The
HTML remains the only source of truth. Generated proofreading files are disposable views of that
source and are never edited.

The first implementation covers the complete `4-freetalking` track. Its unit of review is one
theme containing the Advanced and Intermediate versions together.

## Why the projection is one-way

Automatically merging edited Markdown back into HTML would create two editable sources and make
it easy to overwrite markup or a newer correction. Instead:

1. HTML is projected into compact Markdown and JSONL.
2. Reviewers report proposed changes with an exact source hash and text locator.
3. The issue file is validated against the current HTML.
4. An editor applies approved changes to `lesson.html` explicitly.
5. The projection is regenerated and checked.

If either the lesson hash or current field text changed after extraction, issue validation fails.
The reviewer then uses a newly generated packet instead of guessing how to merge stale prose.

## Generated artifacts

Run:

```sh
python3 korean/tools/build_proofreading_packets.py korean/tracks/4-freetalking
```

This writes `korean/proofreading/4-freetalking/`:

| Artifact | Purpose |
| --- | --- |
| `packets/01-…md` through `10-…md` | One theme per packet, with each Advanced lesson immediately followed by its Intermediate sibling |
| `lessons.jsonl` | One lesson per line, containing exact `source` / `pageId` / `field` locators and source hashes |
| `boilerplate.md` | Every unique text variant from the repeated style and feedback pages omitted from theme packets |
| `manifest.json` | Counts, packet membership, source-set hashes and omitted-page signatures |

The theme packets retain:

- three-language metadata titles;
- the goal, its three axes and Japanese support;
- every model-story or article line, translation, exact Korean highlight span and vocabulary gloss;
- model/article tutor guidance;
- the learner-facing talk introduction;
- all eight Korean/Japanese main questions;
- all eight tutor instructions and twenty-four follow-up questions.

They omit HTML attributes unrelated to locating text, CSS, JavaScript, assets, pager markup,
correction controls and repeated screen chrome. Omitted repeated text is still reviewable once in
`boilerplate.md`.

## Review batches and passes

Use the ten theme packets as the only parallel work boundary. Do not split Advanced and
Intermediate: their adjacency is what makes level drift visible. A reviewer may make several
passes over one packet, but every finding goes into one issue JSONL file for that review round.

Recommended passes:

1. **Korean naturalness:** spoken phrasing, ambiguity, double questions and awkward follow-ups.
2. **Japanese parity:** direct meaning, tone, omissions and vocabulary-gloss consistency.
3. **Question ladder:** concrete warm-up through difficult opinion and a true closing reversal.
4. **Level pairing:** same intent and adult interest, with genuinely lower processing burden in Intermediate.
5. **Repetition:** duplicated stories, main questions or conspicuous follow-ups inside the theme.
6. **Sensitivity:** assumptions, stereotyping, advice or judgment; every `[깊게]` lesson must preserve its range/skip contract.

After the ten packet reviews, run one cross-theme pass over `lessons.jsonl` for repeated strings
and terminology. Structural HTML, runtime behavior and mobile layout remain separate QA jobs;
this text projection does not replace them.

## Review issue format

Store one JSON object per line. Copy `sourceSha256`, `source`, `pageId`, `field` and `current`
exactly from the packet/JSONL. `suggested` contains only the replacement for that one field.

```json
{"source":"korean/tracks/4-freetalking/courses/talk-me-lately-advanced/lessons/01-worth-the-money/lesson.html","sourceSha256":"<64 hex characters>","pageId":"q4","field":"question.ko","current":"현재 질문","suggested":"제안하는 질문","category":"ko-naturalness","severity":"warning","reason":"말할 때 목적어가 불분명하다."}
```

Allowed severities are `error`, `warning` and `suggestion`. Useful categories include
`ko-naturalness`, `ja-parity`, `vocabulary`, `pedagogy`, `level`, `repetition`, `sensitivity`
and `metadata`.

Validate a completed issue file before applying anything:

```sh
python3 korean/tools/build_proofreading_packets.py \
  korean/tracks/4-freetalking \
  --validate-issues path/to/issues.jsonl
```

Validation rejects malformed JSON, missing fields, unknown locators, stale HTML hashes, stale
current text, no-op suggestions and unknown severity values. It never edits lesson files.

If a shared-text or other non-overlapping edit changes a lesson's whole-file hash while review is
in progress, do not hand-edit the hashes. Refresh them with the guarded mode below. It updates
only `sourceSha256`, and only after every cited locator still contains the exact stored `current`
text; any overlapping content edit makes the command fail without writing the issue file.

```sh
python3 korean/tools/build_proofreading_packets.py \
  korean/tracks/4-freetalking \
  --refresh-issue-hashes path/to/issues.jsonl
```

## Applying an approved round

1. Validate and triage the combined issue JSONL. Resolve conflicting suggestions before editing.
2. Edit only the cited source fields in `lesson.html`; paired Korean/Japanese changes normally
   require two explicit issues so neither language changes silently.
3. Verify that every approved suggestion landed in the cited field. This post-edit mode expects
   the stored source hash to be historical and checks `suggested` rather than `current`:

   ```sh
   python3 korean/tools/build_proofreading_packets.py \
     korean/tracks/4-freetalking \
     --verify-applied path/to/issues.jsonl
   ```

   If a later reviewed round improves the same field again, keep the earlier audit record and add
   `"supersededBy":"later.issues.jsonl:LINE"`. Verification accepts that chain only when the
   referenced record cites the same locator, starts from the earlier suggestion, and its final
   suggestion is the text currently in the HTML. This prevents a legitimate second-pass repair
   from making the first audit look unapplied without allowing stale suggestions to be waived.

4. Run the freetalking structural/reference checks and `git diff --check`.
5. Regenerate the packets.
6. Prove they are current:

   ```sh
   python3 korean/tools/build_proofreading_packets.py \
     korean/tracks/4-freetalking --check
   ```

7. Re-run representative 480px browser QA for any correction that materially changes line length,
   article density or a deep-topic instruction.

The round is complete only when issue validation happened before editing, the HTML checks pass,
and `--check` reports all 182 decks and ten packets current.

Packet generation itself also enforces the static deck shell: exact page/source shape, metadata,
unique sync IDs, resolved local `href`/`src` references, eight nonempty bilingual main prompts,
three nonempty follow-ups per prompt, no yomi, and no inline CSS or JavaScript. Main prompts and
follow-ups may legitimately be instructions such as `아침부터 순서대로 이야기해 주세요.` rather
than questions. This keeps the final `--check` from proving text freshness while silently accepting
a structurally damaged deck.
