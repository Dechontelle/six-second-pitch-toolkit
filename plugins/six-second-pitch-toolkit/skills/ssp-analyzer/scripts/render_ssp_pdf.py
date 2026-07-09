#!/usr/bin/env python3
"""
render_ssp_pdf.py — deterministic, good-looking PDF for Six Second Pitch analyses.

Usage:
    python3 render_ssp_pdf.py INPUT.md OUTPUT.pdf

Why this exists: letting each run hand-roll a PDF (e.g. with ReportLab) produced
clipped tables and clipped score boxes. This renders the analysis markdown to HTML
and uses WeasyPrint, which wraps table cells and never lets content run off the page.

Dependencies (auto-checked): weasyprint, markdown.
    pip install weasyprint markdown --break-system-packages
"""

import sys, os, re

def main():
    if len(sys.argv) < 3:
        print("usage: render_ssp_pdf.py INPUT.md OUTPUT.pdf", file=sys.stderr)
        sys.exit(2)
    src, out = sys.argv[1], sys.argv[2]

    try:
        import markdown
        from weasyprint import HTML
    except ImportError as e:
        print(f"Missing dependency: {e}. Run: pip install weasyprint markdown --break-system-packages",
              file=sys.stderr)
        sys.exit(3)

    md = open(src, encoding="utf-8").read()
    lines = md.split("\n")

    # --- Title from the first H1 ---
    title = "Six Second Pitch Analysis"
    brand = ""
    for i, ln in enumerate(lines):
        if ln.startswith("# "):
            h1 = ln[2:].strip()
            # "Brand (Sub) — Six Second Pitch Analysis" -> brand = "Brand (Sub)"
            brand = re.split(r"\s*[—-]\s*Six Second Pitch", h1)[0].strip()
            title = h1
            lines[i] = ""  # remove H1 from body; the cover shows it
            break

    # --- Score + color (graceful if absent) ---
    # Lock onto the CURRENT score, not a historical "Prior runs ... 6.0/10" mention.
    # Priority: "Total: NN/50 -> X.X/10", then "Clarity Score: X.X/10", then first "X.X/10".
    score = None
    score_emoji = None
    patterns = [
        r"Total:.*?(?:→|->|=)\s*(\d{1,2}\.\d)\s*/\s*10\s*(🔴|🟡|🟢)?",
        r"Clarity Score:\s*\**\s*(\d{1,2}\.\d)\s*/\s*10\s*(🔴|🟡|🟢)?",
        r"(\d{1,2}\.\d)\s*/\s*10\s*(🔴|🟡|🟢)",
        r"(\d{1,2}\.\d)\s*/\s*10",
    ]
    for pat in patterns:
        m = re.search(pat, md)
        if m:
            score = m.group(1)
            if m.lastindex and m.lastindex >= 2:
                score_emoji = m.group(2)
            break

    if score_emoji:
        color = {"🔴": "red", "🟡": "amber", "🟢": "green"}[score_emoji]
    elif score is not None:
        # derive from score band if no emoji next to it
        f = float(score)
        color = "red" if f < 4.0 else ("green" if f >= 7.5 else "amber")
    else:
        color = "amber"
    color_label = {"red": "Red", "amber": "Amber", "green": "Green"}[color]

    body_md = "\n".join(lines)

    # --- emoji / glyph -> styled spans (avoids tofu boxes) ---
    def badge(c, label):
        return f'<span class="badge {c}">&#9679; {label}</span>'
    body_md = (body_md
               .replace("🟡", badge("amber", "Amber"))
               .replace("🔴", badge("red", "Red"))
               .replace("🟢", badge("green", "Green"))
               .replace("✔", "&#10003;").replace("✅", "&#10003;")
               .replace("⚠️", '<span class="warn">&#9888;</span>')
               .replace("⚠", '<span class="warn">&#9888;</span>')
               .replace("✓", '<span class="ok">&#10003;</span>'))

    html_body = markdown.markdown(body_md, extensions=["tables", "fenced_code", "sane_lists"])

    score_html = ""
    if score:
        score_html = (f'<div class="scorebox"><div class="scorenum">{score}'
                      f'<span class="den">/10</span></div>'
                      f'<div class="scorelabel"><span class="badge {color}">&#9679; {color_label}</span></div></div>')

    cover = f"""
    <div class="cover">
      <div class="kicker">SIX SECOND PITCH &middot; ANALYSIS</div>
      <h1>{brand or title}</h1>
      {score_html}
      <div class="primer">
        <h3>What the Six Second Pitch measures</h3>
        <p>The Six Second Pitch tests one thing: can a stranger understand <strong>who you help</strong>,
        <strong>what problem you solve</strong>, and <strong>what you deliver</strong> &mdash; in about six seconds?
        It scores the clarity of three variables &mdash; <em>Person, Problem, Promise</em> &mdash; against the formula
        &ldquo;I help [PERSON who has this PROBLEM] [get this PROMISE],&rdquo; then rebuilds the message from the words
        real buyers actually use. Scores run 0&ndash;10:
        <span class="badge red">&#9679;</span> 0&ndash;3.9 structural problem,
        <span class="badge amber">&#9679;</span> 4.0&ndash;7.4 message exists but isn&rsquo;t landing,
        <span class="badge green">&#9679;</span> 7.5&ndash;10 clear and working.</p>
      </div>
    </div>
    <div class="pagebreak"></div>
    """

    css = """
    @page { size: Letter; margin: 1.7cm 1.8cm 2.0cm 1.8cm;
      @bottom-center { content: "Six Second Pitch analysis by Dee Patience  |  Grounded Growth System";
        font-size: 7.5pt; color: #9a8f80; }
      @bottom-right { content: counter(page); font-size: 8pt; color:#9a8f80; } }
    * { box-sizing: border-box; }
    body { font-family: 'DejaVu Sans','Helvetica',sans-serif; font-size: 9.4pt; line-height: 1.5; color: #2b2b2b; }
    h1,h2,h3,h4 { font-family: 'DejaVu Sans','Helvetica',sans-serif; color:#1f3a2e; line-height:1.2; }
    h2 { font-size: 13pt; border-bottom: 2px solid #d8cfc0; padding-bottom: 3px; margin-top: 18px; color:#234; }
    h3 { font-size: 10.6pt; margin-top: 12px; }
    p { margin: 6px 0; }
    /* tables: fixed layout + wrapping so cells NEVER overflow the page */
    table { border-collapse: collapse; width: 100%; table-layout: fixed; margin: 8px 0 12px; font-size: 8.6pt; }
    th { background:#234735; color:#fff; text-align:left; padding:5px 7px; font-weight:600;
         word-wrap:break-word; overflow-wrap:anywhere; }
    td { border:1px solid #ddd; padding:5px 7px; vertical-align:top;
         word-wrap:break-word; overflow-wrap:anywhere; hyphens:auto; }
    /* narrow first column (labels), wide remainder */
    th:first-child, td:first-child { width: 19%; }
    tr:nth-child(even) td { background:#f7f5f0; }
    blockquote { border-left: 3px solid #b89b5e; background:#faf7f0; margin:8px 0; padding:6px 12px; color:#4a4a4a; }
    code { background:#f0ece3; padding:1px 3px; border-radius:3px; font-size:8.4pt; }
    pre { background:#f5f2ec; padding:8px 10px; border-radius:5px; white-space:pre-wrap; word-wrap:break-word; font-size:8pt; }
    hr { border:none; border-top:1px solid #e3dccf; margin:14px 0; }
    ul,ol { margin:6px 0 6px 18px; } li { margin:2px 0; }
    strong { color:#1f3a2e; }
    .badge { font-size:8pt; font-weight:700; padding:1px 6px; border-radius:9px; white-space:nowrap; }
    .badge.amber { background:#fcefcf; color:#9a6b00; }
    .badge.red { background:#fbdcdc; color:#a11; }
    .badge.green { background:#d9f0df; color:#1c6b34; }
    .warn { color:#c08a00; font-weight:700; } .ok { color:#1c6b34; font-weight:700; }
    .pagebreak { page-break-after: always; }
    .cover { padding-top: 18px; }
    .cover .kicker { letter-spacing:3px; font-size:9pt; color:#b89b5e; font-weight:700; }
    .cover h1 { font-size:26pt; margin:6px 0 2px; color:#1f3a2e; border:none; }
    .scorebox { margin:20px 0 14px; }
    .scorenum { font-size:50pt; font-weight:800; color:#234735; line-height:1; display:inline-block; }
    .scorenum .den { font-size:18pt; color:#9a8f80; font-weight:600; }
    .scorelabel { margin-top:6px; font-size:12pt; }
    .primer { background:#f7f5f0; border:1px solid #e3dccf; border-radius:8px; padding:14px 18px; margin-top:10px; }
    .primer h3 { margin:0 0 6px; color:#234735; } .primer p { margin:0; font-size:9pt; color:#4a4a4a; }
    """

    full = (f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{css}</style></head>"
            f"<body>{cover}{html_body}</body></html>")
    HTML(string=full).write_pdf(out)
    print(f"wrote {out}")

if __name__ == "__main__":
    main()
