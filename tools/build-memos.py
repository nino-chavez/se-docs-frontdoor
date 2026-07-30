#!/usr/bin/env python3
"""Build HTML counterparts for the two memos, using the house design tokens
lifted from docs/solution-plan.html. Single-column memo layout: no sidebar,
because a one-page memo does not need navigation."""
import re, sys, html as H

CSS = """
    :root{--violet:#7c3aed;--navy:#1a365d;--ink:#171717;--ink2:#404040;--body:#525252;
      --bg:#ffffff;--bg2:#f5f5f5;--ok:#059669;--warn:#d97706;--info:#0284c7;--rule:#e5e5e5}
    *{margin:0;padding:0;box-sizing:border-box}
    body{font-family:system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
      background:var(--bg2);color:var(--body);line-height:1.65;-webkit-font-smoothing:antialiased}
    .wrap{max-width:820px;margin:0 auto;padding:48px 24px 80px}
    .sheet{background:var(--bg);border-radius:14px;padding:48px 52px;box-shadow:0 1px 3px rgba(0,0,0,.09),0 8px 28px rgba(0,0,0,.04)}
    .eyebrow{font-size:12px;letter-spacing:.09em;text-transform:uppercase;font-weight:700;color:var(--violet);margin-bottom:14px}
    h1{font-size:31px;line-height:1.2;color:var(--ink);margin-bottom:14px;letter-spacing:-.015em}
    .meta{font-size:13.5px;color:var(--ink2);padding-bottom:22px;margin-bottom:32px;border-bottom:2px solid var(--violet)}
    .meta strong{color:var(--ink)}
    h2{font-size:19px;color:var(--violet);margin:36px 0 14px;letter-spacing:-.01em}
    h2:first-of-type{margin-top:0}
    p{margin-bottom:15px;font-size:15.5px}
    strong{color:var(--ink)}
    table{width:100%;border-collapse:collapse;margin:20px 0;font-size:14.5px}
    th,td{padding:11px 13px;text-align:left;border-bottom:1px solid var(--rule);vertical-align:top}
    th{background:var(--bg2);font-weight:650;color:var(--ink);font-size:13px;
      letter-spacing:.03em;text-transform:uppercase}
    td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
    tbody tr:last-child td{border-bottom:none}
    tr.total td{border-top:2px solid var(--rule);font-weight:700;color:var(--ink)}
    tr.flag td{background:#f0fdf4}
    ul{margin:14px 0;padding-left:22px}
    li{margin-bottom:9px;font-size:15.5px}
    .callout{background:#f6f3ff;border-left:4px solid var(--violet);padding:16px 18px;
      border-radius:0 8px 8px 0;margin:22px 0}
    .callout p:last-child{margin-bottom:0}
    .quiet{background:var(--bg2);border-radius:8px;padding:14px 16px;margin:22px 0;font-size:14px}
    .quiet p:last-child{margin-bottom:0}
    .foot{margin-top:40px;padding-top:18px;border-top:1px solid var(--rule);font-size:12.5px;color:#737373}
    .foot code{font-family:'Monaco','Consolas',monospace;font-size:11.5px;color:var(--ink2)}
    .tw{overflow-x:auto;-webkit-overflow-scrolling:touch}
    @media (max-width:640px){.sheet{padding:30px 22px;border-radius:10px}.wrap{padding:20px 12px 48px}h1{font-size:25px}}
    @media print{@page{margin:.6in}body{background:#fff;font-size:11pt}
      .wrap{padding:0;max-width:none}.sheet{box-shadow:none;padding:0;border-radius:0}
      h2{page-break-after:avoid}table,tr{page-break-inside:avoid}
      .callout,.quiet,tr.flag td{print-color-adjust:exact;-webkit-print-color-adjust:exact}}
"""

def esc(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
             .replace('---', '&mdash;').replace(' -- ', ' &mdash; '))

def inline(t):
    t = esc(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*([^*\n]+?)\*(?![\w*])', r'<em>\1</em>', t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    return t

def build(md_path, out_path, title, eyebrow, favicon_note=''):
    src = open(md_path).read()
    lines = src.split('\n')
    out, i = [], 0
    # header block
    h1 = lines[0].lstrip('# ').strip()
    i = 1
    meta = []
    while i < len(lines) and not lines[i].startswith('---'):
        if lines[i].strip():
            meta.append(inline(lines[i].strip()))
        i += 1
    i += 1  # skip ---
    body = []
    while i < len(lines):
        ln = lines[i]
        if ln.startswith('## '):
            body.append(f'<h2>{inline(ln[3:].strip())}</h2>')
            i += 1
        elif ln.startswith('| '):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                rows.append(lines[i]); i += 1
            cells = [[c.strip() for c in r.strip().strip('|').split('|')] for r in rows]
            align = cells[1] if len(cells) > 1 else []
            nums = {j for j, a in enumerate(align) if a.endswith(':')}
            head = cells[0]
            th = ''.join(f'<th{" class=\"num\"" if j in nums else ""}>{inline(c)}</th>'
                         for j, c in enumerate(head))
            trs = []
            for r in cells[2:]:
                cls = ''
                joined = ' '.join(r)
                if r and r[0].startswith('**All') or joined.startswith('**Total'):
                    cls = ' class="total"'
                elif '**' in (r[0] if r else ''):
                    cls = ' class="flag"'
                tds = ''.join(f'<td{" class=\"num\"" if j in nums else ""}>{inline(c)}</td>'
                              for j, c in enumerate(r))
                trs.append(f'<tr{cls}>{tds}</tr>')
            body.append(f'<div class="tw"><table><thead><tr>{th}</tr></thead>'
                        f'<tbody>{"".join(trs)}</tbody></table></div>')
        elif ln.startswith('- '):
            items = []
            while i < len(lines) and lines[i].startswith('- '):
                items.append(f'<li>{inline(lines[i][2:].strip())}</li>'); i += 1
            body.append(f'<ul>{"".join(items)}</ul>')
        elif re.match(r'^\d+\.\s', ln):
            items = []
            while i < len(lines) and re.match(r'^\d+\.\s', lines[i]):
                items.append(f'<li>{inline(re.sub(r"^\d+\.\s+", "", lines[i]).strip())}</li>')
                i += 1
            body.append(f'<ol>{"".join(items)}</ol>')
        elif ln.startswith('<sub>'):
            txt = re.sub(r'</?sub>', '', ln)
            body.append(f'<div class="foot">{inline(txt)}</div>'); i += 1
        elif ln.strip() == '---':
            i += 1
        elif ln.strip():
            para = ln.strip()
            body.append(f'<p>{inline(para)}</p>'); i += 1
        else:
            i += 1
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{H.escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
<div class="wrap"><div class="sheet">
<div class="eyebrow">{H.escape(eyebrow)}</div>
<h1>{inline(h1)}</h1>
<div class="meta">{'<br>'.join(meta)}</div>
{chr(10).join(body)}
</div></div>
</body>
</html>
"""
    open(out_path, 'w').write(doc)
    return out_path

if __name__ == '__main__':
    print(build('docs/memo-leadership.md', 'docs/memo-leadership.html',
                'Knowledge access for Solution Engineering — Leadership', 'Leadership memo'))
    print(build('docs/memo-team.md', 'docs/memo-team.html',
                'SE/SA knowledge access — Team leads', 'Team leads memo'))
