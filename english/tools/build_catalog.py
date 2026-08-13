#!/usr/bin/env python3
"""Build the English review catalog from the three table-of-contents files.

    python3 english/tools/build_catalog.py            # writes english/catalog.html

The catalog exists to be **reviewed**, not browsed. A native speaker's question
is "does anyone actually say this?", so the model sentences are the thing the
page puts in front of them; frames, Core links and the JP-difficulty note are
context sized to stay out of the way.

It holds no facts of its own. Everything comes from:

    tracks/1-core-patterns/table-of-contents.md
    tracks/2-contextual-english/table-of-contents.md
    tracks/3-freetalking/table-of-contents.md

so a wrong line here is a wrong line in a TOC. Re-run after any TOC change.
Never hand-edit `catalog.html`.

Every item gets a stable id — CORE-31, CTX-12, FT-45 — so a reviewer can write
"CORE-31: nobody says that" and it is unambiguous.
"""

import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TRACKS = ROOT / "tracks"
OUT = ROOT / "catalog.html"


def read(p):
    return (TRACKS / p).read_text(encoding="utf-8")


def blocks(text, start_marker=None):
    """Split a TOC into (number, heading, body) per numbered item.

    The heading line may carry trailing markup after the closing `**` — the
    freetalking track puts its format tag there (`**9. Title** `story``) — so
    that tail is captured and appended to the heading rather than anchoring the
    match to end-of-line, which silently matched only one topic in 121.
    """
    if start_marker:
        text = text.split(start_marker, 1)[1]
    parts = re.split(r"^\*\*(\d+)\. (.+?)\*\*(.*)$", text, flags=re.M)
    out = []
    for i in range(1, len(parts), 4):
        out.append((int(parts[i]), parts[i + 1] + parts[i + 2], parts[i + 3]))
    return out


def units(text, pattern):
    """Map item number -> the unit/season/theme heading it sits under."""
    owner, cur = {}, "—"
    for line in text.splitlines():
        h = re.match(pattern, line)
        if h:
            cur = h.group(1).strip()
            continue
        n = re.match(r"^\*\*(\d+)\. ", line)
        if n:
            owner[int(n.group(1))] = cur
    return owner


def field(body, label):
    """Core and Contextual write `- *Label:* ...`; Freetalking omits the dash."""
    m = re.search(rf"^-? ?\*{label}:\* (.+)$", body, re.M)
    return m.group(1).strip() if m else ""


def inline(s):
    """Escape, then re-render the TOC's inline markup as spans."""
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r'<code>\1</code>', s)
    s = re.sub(r"\*\*\(Core ([^)]+)\)\*\*", r'<span class="core">Core \1</span>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
    return s


# ---------------------------------------------------------------- parsers

def parse_core():
    t = read("1-core-patterns/table-of-contents.md")
    owner = units(t, r"^## (Unit \d+ · [^·]+)")
    items = []
    for n, head, body in blocks(t, "# Part 1"):
        title, _, cando_hint = head.partition(" — ")
        lines = [l for l in body.splitlines() if re.match(r'^- ["`]', l)]
        models = []
        for l in lines:
            m = re.match(r'^- "(.+?)" — `(.+?)`(.*)$', l)
            if m:
                models.append((m.group(1), m.group(2), m.group(3)))
        items.append(dict(
            id=f"CORE-{n}", n=n, unit=owner.get(n, "—"),
            title=title.strip(),
            # Core writes `*Can-do: ...*` — asterisks wrap the whole line, not
            # just the label, so field() (which expects `*Label:* value`) misses it.
            cando=(re.search(r"^\*Can-do: (.+?)\*$", body, re.M).group(1)
                   if re.search(r"^\*Can-do: (.+?)\*$", body, re.M) else cando_hint),
            models=models, expr=field(body, "Expressions"),
            gram=field(body, "Grammar"), jp=field(body, "JP"),
            part="Part 2 · unreviewed" if n > 70 else "",
        ))
    return items


def parse_ctx():
    t = read("2-contextual-english/table-of-contents.md")
    owner = units(t, r"^## (Season \d+ · [^·]+)")
    show = units(t, r"^# (Show \d+ · .+)$")
    items = []
    for n, head, body in blocks(t):
        scene = re.search(r"^\*場面: (.+?)\*$", body, re.M)
        cando = re.search(r"^\*Can-do: (.+?)\*$", body, re.M)
        turns = []
        for m in re.finditer(r'^- 私: "(.+?)" — `(.+?)`(.*?)$\n\s*→ (.+?): "(.+?)"', body, re.M):
            turns.append((m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)))
        items.append(dict(
            id=f"CTX-{n}", n=n, unit=owner.get(n, "—"), show=show.get(n, ""),
            title=head.strip(), scene=scene.group(1) if scene else "",
            cando=cando.group(1) if cando else "", turns=turns,
            expr=field(body, "Expressions"), understand=field(body, "Understand"),
        ))
    return items


def parse_ft():
    t = read("3-freetalking/table-of-contents.md")
    owner = units(t, r"^# (Theme \d+ · [^·]+)")
    items = []
    for n, head, body in blocks(t):
        fmt = re.findall(r"`(story|choose|両国|opinion)`", head)
        items.append(dict(
            id=f"FT-{n}", n=n, unit=owner.get(n, "—"),
            title=re.sub(r"\s*`[^`]+`", "", head).split(" — ")[0].strip(),
            fmt=fmt[0] if fmt else "",
            deep="深く" in head,
            # Balance-game topics carry their opening line in the heading as an
            # italic clause instead of an *Opens:* field — see the theme note.
            opens=field(body, "Opens").strip() or (
                (re.search(r"— \*(.+?)\*", head).group(1) if re.search(r"— \*(.+?)\*", head) else "")),
            ladder=field(body, "Ladder"), moves=field(body, "Moves"),
            shared=field(body, "Shared"),
        ))
    return items


# ---------------------------------------------------------------- render

def group(items):
    out, last = [], None
    for it in items:
        if it["unit"] != last:
            out.append(("unit", it.get("show", ""), it["unit"]))
            last = it["unit"]
        out.append(("item", None, it))
    return out


def render_core(items):
    h = []
    for kind, extra, it in group(items):
        if kind == "unit":
            h.append(f'<h3 class="grp">{html.escape(it)}</h3>')
            continue
        rows = "".join(
            f'<div class="say"><p class="model">{html.escape(m)}</p>'
            f'<p class="frame"><code>{html.escape(f)}</code>{inline(tail)}</p></div>'
            for m, f, tail in it["models"])
        meta = "".join(
            f'<p class="meta"><span class="lbl">{lbl}</span>{inline(v)}</p>'
            for lbl, v in (("Expressions", it["expr"]), ("Grammar", it["gram"])) if v)
        jp = f'<p class="jp"><span class="lbl">JP</span>{inline(it["jp"])}</p>' if it["jp"] else ""
        flag = '<span class="flag">unreviewed</span>' if it["part"] else ""
        h.append(
            f'<article class="it" id="{it["id"]}">'
            f'<div class="hd"><a class="rid" href="#{it["id"]}">{it["id"]}</a>'
            f'<h4>{html.escape(it["title"])}</h4>{flag}</div>'
            f'<p class="cando">{html.escape(it["cando"])}</p>{rows}{meta}{jp}</article>')
    return "".join(h)


def render_ctx(items):
    h, lastshow = [], None
    for it in items:
        if it["show"] != lastshow:
            h.append(f'<h2 class="show">{html.escape(it["show"])}</h2>')
            lastshow = it["show"]
        h.append(f'<h3 class="grp">{html.escape(it["unit"])}</h3>' if it["n"] % 6 == 1 else "")
        turns = "".join(
            f'<div class="say"><p class="model"><span class="who">私</span>{html.escape(l)}</p>'
            f'<p class="frame"><code>{html.escape(f)}</code>{inline(tail)}</p>'
            f'<p class="reply"><span class="who">{html.escape(who)}</span>{html.escape(rep)}</p></div>'
            for l, f, tail, who, rep in it["turns"])
        extra = "".join(
            f'<p class="meta"><span class="lbl">{lbl}</span>{inline(v)}</p>'
            for lbl, v in (("Expressions", it["expr"]), ("Understand", it["understand"])) if v)
        h.append(
            f'<article class="it" id="{it["id"]}">'
            f'<div class="hd"><a class="rid" href="#{it["id"]}">{it["id"]}</a>'
            f'<h4>{html.escape(it["title"])}</h4><span class="flag">unreviewed</span></div>'
            f'<p class="scene">{html.escape(it["scene"])}</p>'
            f'<p class="cando">{html.escape(it["cando"])}</p>{turns}{extra}</article>')
    return "".join(h)


def render_ft(items):
    h = []
    for kind, _x, it in group(items):
        if kind == "unit":
            h.append(f'<h3 class="grp">{html.escape(it)}</h3>')
            continue
        tags = (f'<span class="tag">{it["fmt"]}</span>' if it["fmt"] else "") + \
               ('<span class="tag deep">深く</span>' if it["deep"] else "")
        h.append(
            f'<article class="it" id="{it["id"]}">'
            f'<div class="hd"><a class="rid" href="#{it["id"]}">{it["id"]}</a>'
            f'<h4>{html.escape(it["title"])}</h4>{tags}</div>'
            f'<div class="say"><p class="model">{html.escape(it["opens"])}</p></div>'
            f'<p class="meta"><span class="lbl">Ladder</span>{inline(it["ladder"])}</p>'
            + (f'<p class="meta"><span class="lbl">Moves</span>{inline(it["moves"])}</p>' if it["moves"] else "")
            + f'</article>')
    return "".join(h)


def main():
    core, ctx, ft = parse_core(), parse_ctx(), parse_ft()
    counts = (len(core), len(ctx), len(ft))
    if counts != (122, 60, 121):
        print(f"! parsed {counts}, expected (122, 60, 121) — a TOC changed shape "
              f"or the parser is stale", file=sys.stderr)

    tpl = (pathlib.Path(__file__).parent / "catalog_template.html").read_text(encoding="utf-8")
    OUT.write_text(
        tpl.replace("{{CORE}}", render_core(core))
           .replace("{{CTX}}", render_ctx(ctx))
           .replace("{{FT}}", render_ft(ft))
           .replace("{{N_CORE}}", str(len(core)))
           .replace("{{N_CTX}}", str(len(ctx)))
           .replace("{{N_FT}}", str(len(ft)))
           .replace("{{N_ALL}}", str(sum(counts))),
        encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT.parent)} — {counts[0]} lessons, "
          f"{counts[1]} episodes, {counts[2]} topics")
    return 0


if __name__ == "__main__":
    sys.exit(main())
