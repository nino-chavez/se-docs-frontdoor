#!/usr/bin/env python3
"""Fail if a markdown source and its HTML counterpart have drifted.

Written 2026-07-30 after six HTML mirror edits were silently discarded: the
applying script used an all-or-nothing `if not errors: write()` guard, one
anchor failed to match, and the other five were thrown away with it. Nothing
caught it — `reader:check` validates the HTML against its reader contract but
never against its own source, so the plan carried a revision-3 markdown body
and a revision-2 HTML body for several commits.

Checks one direction only: prose present in the .md and absent from the .html.
The reverse is dominated by navigation, headings and generated chrome, which
legitimately exist only in the rendered file.

Tables and code are excluded — they are re-expressed rather than copied.
"""
import html as H
import re
import sys

PAIRS = [
    ('docs/solution-plan.md', 'docs/solution-plan.html'),
    ('docs/memo-leadership.md', 'docs/memo-leadership.html'),
    ('docs/memo-team.md', 'docs/memo-team.html'),
]

MIN_WORDS = 8   # shorter fragments are too generic to match reliably

# Sentences the HTML deliberately renders differently. Each needs a reason:
# presentation improvements are fine, dropped content is not. Match is a
# normalised substring, so a short distinctive fragment is enough.
ALLOWED_DIVERGENCE = {
    'grades because these are not equally strong':
        'HTML renders the six grades as coloured badges rather than inline prose. '
        'Same six grades, same definitions, better scanning.',
}


def strip_markup(text):
    """Remove emphasis and code markers while keeping sentence punctuation, so
    both sides segment at the same places. Stripping after splitting was a bug:
    `**Not buying anything.** A Google...` splits in the HTML (period, space)
    but not in the markdown (period, asterisks, space), inventing drift."""
    text = H.unescape(text)
    for a, b in (('’', "'"), ('‘', "'"), ('“', '"'),
                 ('”', '"'), ('—', ' '), ('–', '-'),
                 ('§', 'S'), (' ', ' ')):
        text = text.replace(a, b)
    text = re.sub(r'[*`_#>|\[\]]', '', text)
    return re.sub(r'[ \t]+', ' ', text)


def norm(text):
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]', ' ', text.lower())).strip()


def sentences(text):
    out = []
    for chunk in re.split(r'(?<=[.!?])\s+|\n{2,}', strip_markup(text)):
        n = norm(chunk)
        if len(n.split()) >= MIN_WORDS:
            out.append(n)
    return out


def md_text(raw):
    raw = re.sub(r'^---\n.*?\n---\n', '', raw, flags=re.S)
    raw = re.sub(r'</?sub>', ' ', raw)
    raw = re.sub(r'^#{1,6} .*$', ' ', raw, flags=re.M)
    raw = re.sub(r'^\*\*(Author|Status|For|Format|Date|Doc type|Derived from)\*\*.*$',
                 ' ', raw, flags=re.M)
    raw = re.sub(r'```.*?```', ' ', raw, flags=re.S)
    raw = re.sub(r'^\s*\|.*$', ' ', raw, flags=re.M)
    raw = re.sub(r'!?\[([^\]]*)\]\([^)]*\)', r'\1', raw)
    return raw


def html_text(raw):
    raw = re.sub(r'<(script|style|head|nav)\b.*?</\1>', ' ', raw, flags=re.S | re.I)
    raw = re.sub(r'<table\b.*?</table>', ' ', raw, flags=re.S | re.I)
    raw = re.sub(r'<!--.*?-->', ' ', raw, flags=re.S)
    # Block closes become breaks so a heading never merges into the paragraph
    # after it and manufacture a sentence that exists in neither document.
    raw = re.sub(r'</(p|div|li|h[1-6]|ul|ol|blockquote)>', '\n\n', raw, flags=re.I)
    return re.sub(r'<[^>]+>', ' ', raw)


def main():
    failures = 0
    for md_path, html_path in PAIRS:
        try:
            md_raw, html_raw = open(md_path).read(), open(html_path).read()
        except FileNotFoundError as e:
            print(f'SKIP  {e.filename} not found')
            continue

        md_sents = sentences(md_text(md_raw))
        html_blob = ' '.join(sentences(html_text(html_raw)))
        missing = [s for s in md_sents if s not in html_blob]
        waived = [s for s in missing
                  if any(k in s for k in ALLOWED_DIVERGENCE)]
        missing = [s for s in missing if s not in waived]

        label = f'{md_path} -> {html_path}'
        if not missing:
            note = f', {len(waived)} waived' if waived else ''
            print(f'OK    {label}  ({len(md_sents)} sentences present{note})')
            continue

        failures += 1
        print(f'DRIFT {label}  ({len(missing)}/{len(md_sents)} missing from HTML)')
        for s in missing[:10]:
            print(f'        "{s[:110]}"')
        if len(missing) > 10:
            print(f'        ... and {len(missing) - 10} more')

    print()
    if failures:
        print(f'parity: FAIL ({failures} pair(s) drifted)')
        return 1
    print('parity: OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())
