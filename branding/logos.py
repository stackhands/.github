"""One family of stackhands tool logos, in the eb-stack mark's style.

For each tool: mark.svg (128 px tile), logo-light.svg and logo-dark.svg
(mark plus wordmark), favicon.svg (32 px). Glyphs are drawn in the same
frame as the eb-stack mark (about 92 x 84 inside an offset of 8,14).
"""

import os
import sys

LIGHT = dict(back1="#CCFBF1", back2="#99F6E4", teal="#0F766E", front="#F8FAFC", ink="#0F172A",
             line="#94A3B8", acc="#EA580C", accInk="#FFF7ED", tile="#F0FDFA", word="#0F172A")
DARK = dict(back1="#134E4A", back2="#115E59", teal="#2DD4BF", front="#0F172A", ink="#E2E8F0",
            line="#64748B", acc="#F97316", accInk="#0F172A", tile="#0B1220", word="#F8FAFC")


def staged(p):
    return f'''
    <rect x="2" y="14" width="40" height="54" rx="6" fill="{p['back2']}" stroke="{p['teal']}" stroke-width="2.5" stroke-dasharray="6 4"/>
    <rect x="10" y="26" width="22" height="5" rx="1.5" fill="{p['teal']}"/>
    <rect x="10" y="36" width="16" height="5" rx="1.5" fill="{p['teal']}" opacity="0.6"/>
    <rect x="50" y="14" width="40" height="54" rx="6" fill="{p['front']}" stroke="{p['ink']}" stroke-width="2.5"/>
    <rect x="58" y="26" width="22" height="5" rx="1.5" fill="{p['teal']}"/>
    <rect x="58" y="36" width="26" height="5" rx="1.5" fill="{p['line']}"/>
    <rect x="58" y="46" width="18" height="5" rx="1.5" fill="{p['line']}"/>
    <circle cx="46" cy="70" r="15" fill="{p['acc']}" stroke="{p['ink']}" stroke-width="2"/>
    <path d="M38 65.5 h15 m-4 -4 l4 4 l-4 4 M54 74.5 h-15 m4 -4 l-4 4 l4 4" stroke="{p['accInk']}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'''


def guard(p):
    pins = "".join(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="1" fill="{p["teal"]}"/>'
        for x, y, w, h in [(24, 2, 4, 8), (36, 2, 4, 8), (48, 2, 4, 8), (24, 62, 4, 8), (36, 62, 4, 8),
                           (48, 62, 4, 8), (8, 18, 8, 4), (8, 30, 8, 4), (8, 42, 8, 4), (60, 18, 8, 4),
                           (60, 30, 8, 4), (60, 42, 8, 4)])
    return f'''
    {pins}
    <rect x="16" y="10" width="44" height="52" rx="6" fill="{p['back2']}" stroke="{p['teal']}" stroke-width="2.5"/>
    <rect x="25" y="20" width="26" height="30" rx="3" fill="{p['front']}" stroke="{p['ink']}" stroke-width="2"/>
    <rect x="30" y="27" width="16" height="4" rx="1.5" fill="{p['teal']}"/>
    <rect x="30" y="36" width="11" height="4" rx="1.5" fill="{p['line']}"/>
    <path d="M70 40 l18 7 v13 c0 11 -8 19 -18 23 c-10 -4 -18 -12 -18 -23 v-13 z" fill="{p['acc']}" stroke="{p['ink']}" stroke-width="2" stroke-linejoin="round"/>
    <path d="M62 61 l6 6 l11 -12" stroke="{p['accInk']}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'''


def keeplogs(p):
    return f'''
    <rect x="22" y="4" width="50" height="62" rx="6" fill="{p['back1']}" stroke="{p['teal']}" stroke-width="2.5"/>
    <rect x="14" y="12" width="50" height="62" rx="6" fill="{p['back2']}" stroke="{p['teal']}" stroke-width="2.5"/>
    <rect x="6" y="20" width="50" height="62" rx="6" fill="{p['front']}" stroke="{p['ink']}" stroke-width="2.5"/>
    <rect x="14" y="32" width="12" height="5" rx="1.5" fill="{p['acc']}"/>
    <rect x="29" y="32" width="19" height="5" rx="1.5" fill="{p['line']}"/>
    <rect x="14" y="42" width="30" height="5" rx="1.5" fill="{p['line']}"/>
    <rect x="14" y="52" width="24" height="5" rx="1.5" fill="{p['line']}"/>
    <circle cx="70" cy="64" r="15" fill="{p['acc']}" stroke="{p['ink']}" stroke-width="2"/>
    <path d="M70 55 v10 m-5 -5 l5 5 l5 -5 M62 70 v3 h16 v-3" stroke="{p['accInk']}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'''


def common(p):
    return f'''
    <path d="M18 24 L46 46 M76 24 L46 46 M46 46 L46 66" stroke="{p['teal']}" stroke-width="3" stroke-linecap="round"/>
    <rect x="2" y="8" width="32" height="22" rx="5" fill="{p['back1']}" stroke="{p['teal']}" stroke-width="2.5"/>
    <rect x="60" y="8" width="32" height="22" rx="5" fill="{p['back2']}" stroke="{p['teal']}" stroke-width="2.5"/>
    <rect x="30" y="62" width="32" height="22" rx="5" fill="{p['front']}" stroke="{p['ink']}" stroke-width="2.5"/>
    <rect x="9" y="17" width="14" height="4" rx="1.5" fill="{p['teal']}"/>
    <rect x="67" y="17" width="18" height="4" rx="1.5" fill="{p['teal']}"/>
    <rect x="37" y="71" width="16" height="4" rx="1.5" fill="{p['line']}"/>
    <circle cx="46" cy="44" r="15" fill="{p['acc']}" stroke="{p['ink']}" stroke-width="2"/>
    <path d="M39.5 37.5 h13 l-13 13 h13" stroke="{p['accInk']}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'''


def local(p):
    return f'''
    <rect x="16" y="4" width="62" height="12" rx="4" fill="{p['back1']}" stroke="{p['teal']}" stroke-width="2.5"/>
    <rect x="10" y="20" width="62" height="12" rx="4" fill="{p['back2']}" stroke="{p['teal']}" stroke-width="2.5"/>
    <path d="M8 38 h20 l6 6 h40 a4 4 0 0 1 4 4 v30 a4 4 0 0 1 -4 4 h-66 a4 4 0 0 1 -4 -4 v-36 a4 4 0 0 1 4 -4 z" fill="{p['front']}" stroke="{p['ink']}" stroke-width="2.5" stroke-linejoin="round"/>
    <rect x="14" y="56" width="26" height="5" rx="1.5" fill="{p['teal']}"/>
    <rect x="14" y="66" width="18" height="5" rx="1.5" fill="{p['line']}"/>
    <circle cx="74" cy="64" r="15" fill="{p['acc']}" stroke="{p['ink']}" stroke-width="2"/>
    <path d="M66 65 l8 -7 l8 7 M68.5 63 v8 h11 v-8" stroke="{p['accInk']}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'''


def merkle(p):
    leaves = "".join(
        f'<rect x="{x}" y="64" width="18" height="18" rx="4" fill="{p["front"]}" stroke="{p["ink"]}" stroke-width="2.5"/>'
        for x in (2, 26, 50, 74))
    return f'''
    <path d="M47 20 L24 44 M47 20 L70 44 M24 44 L11 64 M24 44 L35 64 M70 44 L59 64 M70 44 L83 64" stroke="{p['teal']}" stroke-width="3" stroke-linecap="round"/>
    {leaves}
    <circle cx="24" cy="44" r="9" fill="{p['back2']}" stroke="{p['teal']}" stroke-width="2.5"/>
    <circle cx="70" cy="44" r="9" fill="{p['back2']}" stroke="{p['teal']}" stroke-width="2.5"/>
    <circle cx="47" cy="18" r="15" fill="{p['acc']}" stroke="{p['ink']}" stroke-width="2"/>
    <path d="M40 18 l5 5 l9 -10" stroke="{p['accInk']}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'''


TOOLS = {
    "eb-staged-rebuild": (staged, "staged rebuild: a staged tree exchanged with the live one"),
    "eessi-arch-guard": (guard, "a CPU die guarded by a shield"),
    "eb-keep-logs": (keeplogs, "log pages kept into a tray"),
    "zig-common": (common, "one shared core wired to three tools"),
    "eb-local": (local, "EESSI layers above a folder you own"),
    "rfc9162": (merkle, "a Merkle tree with a verified root"),
}

FONT = "ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"


def mark(name, glyph, desc, p, tile):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 128 128" fill="none" role="img" aria-labelledby="{name}-mark-title">
  <title id="{name}-mark-title">{name} mark</title>
  <desc>{desc}</desc>
  <rect width="128" height="128" rx="28" fill="{tile}"/>
  <g transform="translate(17,20)">{glyph(p)}
  </g>
</svg>
'''


def wordmark(name, glyph, desc, p, theme):
    width = 128 + int(26.5 * len(name)) + 16
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="120" viewBox="0 0 {width} 120" fill="none" role="img" aria-labelledby="{name}-logo-{theme}">
  <title id="{name}-logo-{theme}">{name}</title>
  <desc>{name} logo ({theme} theme): {desc}, with the wordmark {name}.</desc>
  <g transform="translate(8,14)">{glyph(p)}
  </g>
  <text x="120" y="78" font-family="{FONT}" font-size="48" font-weight="800" letter-spacing="-1.5" fill="{p['word']}">{name}</text>
</svg>
'''


def favicon(name, glyph, p):
    # The glyph at a quarter scale on a teal tile.
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 128 128" role="img" aria-label="{name}">
  <rect width="128" height="128" rx="28" fill="{LIGHT['tile']}" stroke="{LIGHT['teal']}" stroke-width="6"/>
  <g transform="translate(17,20)">{glyph(p)}
  </g>
</svg>
'''


def main(out):
    for name, (glyph, desc) in TOOLS.items():  # eb-stack keeps its own mark
        d = os.path.join(out, name)
        os.makedirs(d, exist_ok=True)
        files = {
            "mark.svg": mark(name, glyph, desc, LIGHT, LIGHT["tile"]),
            "mark-dark.svg": mark(name, glyph, desc, DARK, DARK["tile"]),
            "logo-light.svg": wordmark(name, glyph, desc, LIGHT, "light"),
            "logo-dark.svg": wordmark(name, glyph, desc, DARK, "dark"),
            "favicon.svg": favicon(name, glyph, LIGHT),
        }
        for fname, text in files.items():
            with open(os.path.join(d, fname), "w") as handle:
                handle.write(text)


if __name__ == "__main__":
    main(sys.argv[1])
