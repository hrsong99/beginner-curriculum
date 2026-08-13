#!/usr/bin/env python3
"""Static checks for lesson decks — the ones that otherwise fail silently.

    python3 english/tools/check_deck.py english/tracks            # a tree
    python3 english/tools/check_deck.py path/to/lesson.html ...   # named decks
    python3 english/tools/check_deck.py --all                     # every deck in the repo

Why this exists
---------------
A deck can be valid HTML, pass every reference check, render without a console
error, and still be wrong on screen. Two defects in particular leave no trace,
and the first English deck shipped both:

1. **Tutor script sentence parity.** `runtime/js/script-lines.js` rebuilds the
   blue box as one sentence per line, each with its own translation underneath —
   but only when both sides have the same number of sentences. When they differ
   it deliberately does nothing, because mis-pairing would print "this
   translation belongs to this line" as a lie. The failure therefore looks like
   slightly ugly prose rather than anything broken. `AUTHORING.md` §2 has always
   required the two sides to be the same sentences; nothing enforced it.

2. **Reorder chunking consistency.** Four chunks is the ceiling and the working
   default, three is allowed when a sentence honestly holds three — but the
   criterion has to be the same down the page. Mixed counts on one page are the
   symptom of two criteria, which is what the rule exists to stop.

Neither is caught by reading markup, which is why they are here rather than in a
checklist. A checklist item only reaches the writers who were told to read it.

Exit status is 1 if any ERROR was found. WARNs do not fail the run: they mark
things a human should look at and may legitimately sign off on.
"""

import argparse
import pathlib
import re
import sys
from collections import Counter

import vocabulary

REPO = pathlib.Path(__file__).resolve().parent.parent.parent

EN_END = ".!?"
JA_END = "。！？"
KO_END = ".!?"          # Korean decks punctuate the spoken line with ASCII too

TAG = re.compile(r"<[^>]+>")
PAGE_ID = re.compile(r'data-page-id="([^"]+)"')
SYNC_ID = re.compile(r'data-sync-id="([^"]+)"')
SUBTITLE = re.compile(r'<p class="section-subtitle([^"]*)"[^>]*>(.*?)</p>', re.S)
SPAN_KO = re.compile(r'<span class="ko">(.*?)</span>', re.S)
SPAN_JA = re.compile(r'<span class="ja">(.*?)</span>', re.S)
TASK_BLOCK = re.compile(r'<div class="task-block">')
CHOICE = re.compile(r'class="choice"')
LOCAL_REF = re.compile(r'(?:href|src)="((?!https?:|data:|#)[^"]+)"')
INLINE_STYLE = re.compile(r"<style[\s>]")
INLINE_SCRIPT = re.compile(r"<script(?![^>]*\ssrc=)[^>]*>")


def sentences(text, enders):
    """Count sentences the way script-lines.js does: one per terminal mark."""
    plain = TAG.sub("", text)
    n = sum(1 for ch in plain if ch in enders)
    return n or 1


def pages(html):
    """Split a deck into (page_id, chunk) by data-page-id boundaries."""
    marks = [(m.start(), m.group(1)) for m in PAGE_ID.finditer(html)]
    for i, (pos, pid) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(html)
        yield pid, html[pos:end]


def check(path):
    """Return (errors, warnings) for one deck."""
    html = path.read_text(encoding="utf-8")
    errs, warns = [], []
    is_english = "english/tracks" in path.as_posix()

    # ---- identity and metadata -------------------------------------------
    if 'name="google" content="notranslate"' not in html:
        errs.append("missing <meta name=\"google\" content=\"notranslate\"> — "
                    "Chrome will auto-translate and mangle the mixed content")
    m = re.search(r'name="podo:lesson-id" content="([^"]+)"', html)
    if not m:
        errs.append("missing podo:lesson-id")
    elif "lessons" in path.parts and m.group(1) != path.parent.name:
        # The id must equal its directory only for a deck placed in a course, which
        # is what the production importer reads. A track-root sample-lesson.html is
        # a cut of the canonical trial deck and has no course directory to match.
        errs.append(f"podo:lesson-id {m.group(1)!r} != directory {path.parent.name!r}")
    if is_english and not re.search(r'name="podo:review-id" content="(?:CORE|CTX|FT)-\d+"', html):
        errs.append("missing or invalid podo:review-id — use the stable TOC id")

    # ---- references resolve ----------------------------------------------
    for ref in sorted(set(LOCAL_REF.findall(html))):
        if not (path.parent / ref).exists():
            errs.append(f"broken ref: {ref}")

    # ---- unique ids -------------------------------------------------------
    for label, rx in (("page", PAGE_ID), ("sync", SYNC_ID)):
        dupes = [k for k, n in Counter(rx.findall(html)).items() if n > 1]
        if dupes:
            errs.append(f"duplicate {label} id(s): {', '.join(sorted(dupes))}")

    # ---- deck ships no CSS or JS of its own -------------------------------
    if INLINE_STYLE.search(html):
        errs.append("inline <style> — component CSS belongs in the shared runtime")
    if INLINE_SCRIPT.search(html):
        errs.append("inline <script> — behaviour belongs in the shared runtime")

    # ---- English decks carry no readings ----------------------------------
    if is_english:
        if 'class="yomi"' in html:
            errs.append("`.yomi` in an English deck — katakana over English installs "
                        "the error instead of scaffolding the word (see english/AGENTS.md)")
        if re.search(r"<script[^>]*yomi\.js", html):
            errs.append("English deck loads yomi.js")

        # ---- vocabulary ownership and load -------------------------------
        try:
            vocab = vocabulary.parse(html, source=path)
        except vocabulary.VocabularyError as exc:
            errs.append(str(exc).removeprefix(f"{path}: "))
        else:
            if vocab["status"] != "reviewed":
                errs.append(
                    f"vocabulary status is {vocab['status']!r} — classify the deck's "
                    "new, recycled, assumed-known and receptive-only words"
                )
            capped_track = any(part in {"1-core-patterns", "2-contextual-english"} for part in path.parts)
            load = vocabulary.load_result(vocab) if capped_track else None
            if load:
                (warns if load[0] == "warning" else errs).append(load[1])
            declared = {
                entry["english"].casefold()
                for entries in vocab["categories"].values()
                for entry in entries
            }
            try:
                hints = vocabulary.hint_words(html)
            except vocabulary.VocabularyError as exc:
                errs.append(str(exc))
            else:
                undeclared = sorted(hints - declared)
                if undeclared:
                    errs.append(
                        "hint-chip vocabulary missing from the ownership declaration: "
                        + ", ".join(undeclared)
                    )

    # ---- 1 · tutor script sentence parity ---------------------------------
    for pid, chunk in pages(html):
        for cls, body in SUBTITLE.findall(chunk):
            if "pattern-meaning" in cls:
                continue          # owns its own pairing; script-lines.js skips it
            ko, ja = SPAN_KO.search(body), SPAN_JA.search(body)
            if not (ko and ja):
                continue
            a = sentences(ko.group(1), EN_END if is_english else KO_END)
            b = sentences(ja.group(1), JA_END)
            if a != b:
                errs.append(
                    f"{pid}: tutor script sentence counts differ "
                    f"({'EN' if is_english else 'KO'}={a} JA={b}) — script-lines.js "
                    f"will silently leave the box unsplit")

    # ---- 2 · reorder chunking consistency ---------------------------------
    for pid, chunk in pages(html):
        if "reorder" not in pid:
            continue
        blocks = TASK_BLOCK.split(chunk)[1:]
        counts = [len(CHOICE.findall(b)) for b in blocks]
        if not counts:
            continue
        if len(set(counts)) > 1:
            errs.append(
                f"{pid}: mixed chip counts {counts} on one page — four is the "
                f"ceiling and working default, three is allowed only when a "
                f"sentence honestly holds three, and the criterion must be the "
                f"same down the page")
        elif counts[0] > 4:
            errs.append(f"{pid}: {counts[0]} chips — four is the ceiling")
        elif counts[0] < 3:
            warns.append(f"{pid}: {counts[0]} chips per sentence — confirm no "
                         f"fourth unit is glued to a neighbour")

    return errs, warns


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", help="deck files or directories to scan")
    ap.add_argument("--all", action="store_true", help="scan every deck in the repo")
    args = ap.parse_args()

    targets = []
    # resolve() so a relative argument still reports a repo-relative path below
    roots = [REPO] if args.all else [pathlib.Path(p).resolve() for p in args.paths]
    if not roots:
        ap.error("give a path, or --all")
    for r in roots:
        if r.is_dir():
            targets += sorted(p for p in r.rglob("*.html")
                              if "_archive" not in p.parts and p.name != "viewer.html")
        elif r.exists():
            targets.append(r)
        else:
            print(f"! no such path: {r}", file=sys.stderr)

    decks = [p for p in targets if PAGE_ID.search(p.read_text(encoding="utf-8"))]
    n_err = n_warn = 0
    for deck in decks:
        errs, warns = check(deck)
        n_err += len(errs)
        n_warn += len(warns)
        if errs or warns:
            try:
                label = deck.relative_to(REPO)
            except ValueError:
                label = deck
            print(f"\n{label}")
            for e in errs:
                print(f"  ✗ {e}")
            for w in warns:
                print(f"  ! {w}")

    print(f"\n{len(decks)} deck(s) checked · {n_err} error(s) · {n_warn} warning(s)")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
