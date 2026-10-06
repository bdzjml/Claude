"""Génère les 10 scènes génériques des cartes (630x880, zone visible environ y 90-540)."""
import math
import random
from pathlib import Path

I, G, R, B = "#22170e", "#c9973a", "#8e2a1e", "#3f6c9e"
OUT = Path(__file__).resolve().parent.parent / "illustrations"

FIGURES = f"""
<g id="soldier">
  <path d="M-10 0 L-8 -40 L-14 -42 L-12 -70 Q0 -78 12 -70 L14 -42 L8 -40 L10 0 L3 0 L0 -30 L-3 0Z"/>
  <circle cy="-80" r="9"/><path d="M-11 -82 Q0 -98 11 -82Z"/>
  <rect x="16" y="-122" width="3" height="124"/><path d="M17.5 -136 L22 -122 L13 -122Z" fill="{G}"/>
  <path d="M-26 -66 H-8 V-44 Q-8 -30 -17 -26 Q-26 -30 -26 -44Z"/>
</g>
<g id="warrior">
  <path d="M-14 -70 Q-28 -30 -24 0 H24 Q28 -30 14 -70Z" fill="{R}"/>
  <path d="M-12 0 L-10 -40 L-16 -44 L-14 -72 Q0 -80 14 -72 L16 -44 L10 -40 L12 0 L4 0 L0 -28 L-4 0Z"/>
  <circle cy="-84" r="10"/><path d="M-10 -88 Q0 -104 10 -88Z"/>
  <path d="M12 -66 L56 -132 L61 -128 L18 -62Z" fill="{G}"/><path d="M8 -70 L22 -58" stroke="{I}" stroke-width="5"/>
</g>
<g id="mage">
  <path d="M0 -92 Q-14 -90 -16 -72 L-30 0 H30 L16 -72 Q14 -90 0 -92Z"/>
  <path d="M0 -112 Q-16 -110 -16 -90 Q-10 -76 0 -76 Q10 -76 16 -90 Q16 -110 0 -112Z"/>
  <rect x="24" y="-130" width="3" height="130"/>
  <circle cx="25.5" cy="-136" r="9" fill="#9fd0ff"/><circle cx="25.5" cy="-136" r="22" fill="#9fd0ff" opacity=".25"/>
  <path d="M14 -60 L26 -66" stroke="{I}" stroke-width="6"/>
</g>
<g id="rider">
  <path d="M-46 -56 Q-72 -50 -68 -18 Q-60 -40 -44 -46Z"/>
  <path d="M-50 -20 L-46 -42 Q-50 -62 -30 -64 L20 -64 Q34 -64 40 -80 L52 -100 L60 -98 L64 -86 Q58 -78 54 -70 Q48 -56 40 -46 L44 0 L37 0 L32 -36 L-30 -36 L-36 0 L-43 0 L-40 -32Z"/>
  <path d="M-8 -64 L-6 -100 Q4 -110 14 -100 L14 -64Z"/><circle cx="4" cy="-114" r="8"/>
  <path d="M-6 -96 Q-30 -90 -40 -70 Q-20 -82 -4 -84Z" fill="{R}"/>
</g>
<g id="dragon">
  <path d="M0 0 L-160 -140 L-136 -70 L-196 -78 L-140 -14 L-200 0 L-110 40Z"/>
  <path d="M0 0 L160 -140 L136 -70 L196 -78 L140 -14 L200 0 L110 40Z"/>
  <path d="M0 0 L-160 -140 M0 0 L-196 -78 M0 0 L160 -140 M0 0 L196 -78" stroke="{G}" stroke-width="2" opacity=".7"/>
  <path d="M-55 20 Q0 -14 55 20 Q72 80 34 130 Q0 150 -34 130 Q-72 80 -55 20Z"/>
  <path d="M-12 14 Q-20 -40 2 -76 Q24 -102 44 -92 L72 -96 L56 -82 L62 -72 L36 -68 Q22 -56 18 -30 Q16 -6 16 14Z"/>
  <circle cx="38" cy="-84" r="3.5" fill="{G}"/>
  <path d="M-20 136 Q-80 180 -140 160 Q-160 156 -170 168 Q-130 184 -100 184 Q-40 182 10 140Z"/>
</g>
<g id="erdtree">
  <circle cy="-120" r="150" fill="url(#treeglow)"/>
  <path d="M-8 0 Q-4 -60 -10 -90 Q-14 -110 0 -130 Q14 -110 10 -90 Q4 -60 8 0Z" fill="{G}"/>
  <g fill="{G}"><circle cy="-150" r="44"/><circle cx="-40" cy="-130" r="32"/><circle cx="40" cy="-130" r="32"/>
  <circle cx="-26" cy="-180" r="28"/><circle cx="26" cy="-180" r="28"/><circle cy="-200" r="24"/>
  <circle cx="-66" cy="-108" r="20"/><circle cx="66" cy="-108" r="20"/></g>
</g>
<g id="castle">
  <path d="M-110 0 V-70 H-98 V-82 H-86 V-70 H-74 V-82 H-62 V-70 H-50 V-110 H-40 V-122 H-30 V-110 H-20 V-160 L0 -200 L20 -160 V-110 H30 V-122 H40 V-110 H50 V-70 H62 V-82 H74 V-70 H86 V-82 H98 V-70 H110 V0Z"/>
  <path d="M0 -200 V-226" stroke="{I}" stroke-width="3"/><path d="M0 -226 L26 -219 L0 -212Z" fill="{R}"/>
  <g fill="{G}"><rect x="-4" y="-150" width="8" height="14" rx="4"/><rect x="-80" y="-56" width="6" height="10" rx="3"/><rect x="74" y="-56" width="6" height="10" rx="3"/></g>
</g>
"""

HEAD = """<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 630 880" width="630" height="880">
<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{s0}"/><stop offset="1" stop-color="{s1}"/></linearGradient>
  <radialGradient id="sun" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{sun}" stop-opacity=".95"/><stop offset=".35" stop-color="{sun}" stop-opacity=".45"/><stop offset="1" stop-color="{sun}" stop-opacity="0"/></radialGradient>
  <radialGradient id="treeglow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffe7a8" stop-opacity=".8"/><stop offset="1" stop-color="#ffe7a8" stop-opacity="0"/></radialGradient>
  <radialGradient id="vig" cx=".5" cy=".4" r=".8"><stop offset=".5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".6"/></radialGradient>
  <pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(35)"><line x1="0" y1="0" x2="0" y2="6" stroke="#000" stroke-width="1.4" stroke-opacity=".35"/></pattern>
  <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="3"/><feColorMatrix values="0 0 0 0 .15  0 0 0 0 .1  0 0 0 0 .05  0 0 0 .22 0"/></filter>
""" + FIGURES + """
</defs>
<rect width="630" height="880" fill="url(#sky)"/>
"""

FOOT = """
<rect width="630" height="880" filter="url(#grain)"/>
<rect width="630" height="880" fill="url(#vig)"/>
</svg>
"""

def use(ref, x, y, s=1.0, fill=I, flip=False):
    sx = -s if flip else s
    return f'<use href="#{ref}" xlink:href="#{ref}" transform="translate({x} {y}) scale({sx} {s})" fill="{fill}"/>'

def ridge(y, amp, color, seed, step=40, extra=""):
    rnd = random.Random(seed)
    pts = " ".join(f"L{x} {y - rnd.uniform(0, amp):.0f}" for x in range(0, 671, step))
    return f'<path d="M-20 880 L-20 {y} {pts} L650 880Z" fill="{color}" {extra}/>'

def peaks(base, color, seed, n=6, hmin=80, hmax=200, snow=None):
    rnd = random.Random(seed)
    out, x = [], -40
    while x < 670:
        w = rnd.uniform(90, 170); h = rnd.uniform(hmin, hmax)
        out.append(f'<path d="M{x:.0f} {base} L{x + w / 2:.0f} {base - h:.0f} L{x + w:.0f} {base}Z" fill="{color}"/>')
        if snow:
            out.append(f'<path d="M{x + w / 2 - w * .14:.0f} {base - h * .72:.0f} L{x + w / 2:.0f} {base - h:.0f} L{x + w / 2 + w * .14:.0f} {base - h * .72:.0f} L{x + w / 2:.0f} {base - h * .78:.0f}Z" fill="{snow}"/>')
        x += w * .7
    return "".join(out)

def specks(color, seed, n=60, y0=90, y1=520, rmax=2.2):
    rnd = random.Random(seed)
    return "".join(f'<circle cx="{rnd.uniform(40, 590):.0f}" cy="{rnd.uniform(y0, y1):.0f}" r="{rnd.uniform(.5, rmax):.1f}" fill="{color}" opacity="{rnd.uniform(.4, .95):.2f}"/>' for _ in range(n))

def rain(seed):
    rnd = random.Random(seed)
    return "".join(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x - 12:.0f}" y2="{y + 34:.0f}" stroke="#d8dde6" stroke-opacity=".35" stroke-width="1.5"/>'
                   for x, y in ((rnd.uniform(0, 660), rnd.uniform(60, 560)) for _ in range(110)))

def dead_tree(x, y, s, color=I):
    return f'''<g transform="translate({x} {y}) scale({s})" stroke="{color}" stroke-linecap="round" fill="none">
  <path d="M0 0 Q4 -50 -4 -90 Q-8 -120 10 -150" stroke-width="12"/>
  <path d="M-3 -80 Q-40 -100 -60 -140 M2 -110 Q30 -120 50 -160 M-6 -60 Q20 -70 40 -80 M8 -140 Q-10 -170 -20 -190" stroke-width="5"/>
</g>'''

SCENES = {
"01-plaine-arbre": dict(s0="#f6e2a8", s1="#e3a564", sun="#fff1c4", body=lambda: f"""
<circle cx="430" cy="300" r="260" fill="url(#sun)"/>
{use("erdtree", 430, 420, 1.15)}
{peaks(440, "#b98a5e", 11, hmin=40, hmax=110)}
{ridge(450, 30, "#7d5a3a", 12)}
<g fill="#4a3322"><rect x="110" y="380" width="14" height="80"/><rect x="146" y="400" width="14" height="60"/><path d="M100 380 H134 V370 H100Z M136 400 H170 V390 H136Z"/></g>
{ridge(500, 24, "#3a2716", 13)}
<rect x="0" y="500" width="630" height="380" fill="url(#hatch)"/>
{use("rider", 250, 520, 1.25)}
{specks("#fff1c4", 14, 40, 120, 420, 1.8)}"""),
"02-soldats": dict(s0="#f0b070", s1="#9a3b22", sun="#ffd38a", body=lambda: f"""
<circle cx="315" cy="360" r="200" fill="url(#sun)"/>
<circle cx="315" cy="370" r="70" fill="#ffd38a" opacity=".9"/>
{peaks(430, "#7a3a26", 21, hmin=30, hmax=90)}
{ridge(470, 10, I, 22, step=60)}
{"".join(use("soldier", x, 474 - (abs(x - 315) * .04), 1.0 + (0.12 if i % 2 else 0)) for i, x in enumerate(range(95, 560, 66)))}
<g fill="{R}"><path d="M161 340 V300 H196 L188 315 L196 330 H161Z"/><path d="M425 340 V300 H460 L452 315 L460 330 H425Z"/></g>
<path d="M161 474 V300 M425 474 V300" stroke="{I}" stroke-width="3"/>
<rect x="0" y="476" width="630" height="404" fill="{I}"/>"""),
"03-dragon": dict(s0="#8d8f94", s1="#d8b47a", sun="#ffe2a0", body=lambda: f"""
<circle cx="200" cy="420" r="220" fill="url(#sun)"/>
<g fill="#6b6d72" opacity=".7"><ellipse cx="140" cy="150" rx="140" ry="34"/><ellipse cx="480" cy="190" rx="170" ry="40"/></g>
{use("dragon", 400, 250, .95)}
<path d="M396 166 L440 150 L428 170 L480 154" stroke="{G}" stroke-width="5" fill="none"/>
{peaks(470, "#5b4a38", 31, hmin=40, hmax=120)}
<path d="M-20 880 L-20 470 L80 440 L170 460 L240 500 L650 520 L650 880Z" fill="{I}"/>
{use("warrior", 130, 448, 1.05)}"""),
"04-mage-lune": dict(s0="#101a30", s1="#3f5d82", sun="#dfe9ff", body=lambda: f"""
{specks("#f3ecd2", 41, 90, 90, 360, 1.6)}
<circle cx="420" cy="210" r="170" fill="url(#sun)"/>
<circle cx="420" cy="210" r="68" fill="#eef2fb"/>
<circle cx="398" cy="196" r="12" fill="#c9d3e6"/><circle cx="440" cy="232" r="16" fill="#c9d3e6"/>
{peaks(410, "#1c2a44", 42, hmin=30, hmax=100)}
<path d="M520 410 V300 L532 270 L544 300 V410Z M480 410 V340 H500 V410Z" fill="#141e33"/>
<rect x="0" y="410" width="630" height="470" fill="#24395a"/>
{"".join(f'<line x1="{x}" y1="{y}" x2="{x + 60}" y2="{y}" stroke="#c9d3e6" stroke-opacity=".5" stroke-width="2"/>' for x, y in [(380,430),(410,450),(360,470),(430,490),(395,510)])}
<path d="M-20 880 L-20 400 Q60 380 130 420 Q190 450 220 520 L240 880Z" fill="#0c1220"/>
{use("mage", 120, 418, 1.35, fill="#0c1220")}"""),
"05-chevalier-cheval": dict(s0="#f3d9a0", s1="#c9874f", sun="#fff3cf", body=lambda: f"""
<circle cx="470" cy="250" r="230" fill="url(#sun)"/>
{use("erdtree", 500, 400, .6)}
{peaks(420, "#a87b52", 51, hmin=30, hmax=90)}
{ridge(450, 20, "#6e4a2c", 52)}
<rect x="0" y="470" width="630" height="410" fill="#3a2716"/>
<rect x="0" y="470" width="630" height="410" fill="url(#hatch)"/>
<path d="M326 380 L470 300" stroke="{I}" stroke-width="5"/><path d="M470 300 L486 290 L476 306Z" fill="{G}"/>
<path d="M420 328 L440 318 L446 336 L426 346Z" fill="{R}"/>
{use("rider", 300, 500, 1.7)}
<g stroke="#3a2716" stroke-width="3" opacity=".6"><path d="M180 496 Q160 500 140 496 M200 486 Q170 490 150 484"/></g>"""),
"06-duel": dict(s0="#d98c4a", s1="#5b2a1a", sun="#ffc77a", body=lambda: f"""
<circle cx="315" cy="300" r="240" fill="url(#sun)"/>
<path d="M150 470 V220 Q150 140 315 130 Q480 140 480 220 V470 H440 V230 Q440 180 315 172 Q190 180 190 230 V470Z" fill="#3c2014"/>
<path d="M150 220 Q150 140 315 130 Q480 140 480 220" stroke="{G}" stroke-width="3" fill="none" opacity=".6"/>
{ridge(470, 8, I, 61, step=70)}
<rect x="0" y="474" width="630" height="406" fill="{I}"/>
{use("warrior", 250, 476, 1.4)}
{use("warrior", 380, 476, 1.4, flip=True)}
{"".join(f'<line x1="315" y1="300" x2="{315 + 40 * math.cos(a):.0f}" y2="{300 + 40 * math.sin(a):.0f}" stroke="#ffe7a8" stroke-width="3"/>' for a in [k * math.pi / 6 for k in range(12)])}
<circle cx="315" cy="300" r="8" fill="#fff3cf"/>"""),
"07-caelid": dict(s0="#5c1510", s1="#c4532e", sun="#ffb27a", body=lambda: f"""
<circle cx="200" cy="230" r="160" fill="url(#sun)"/>
<circle cx="200" cy="230" r="50" fill="#f6c39a" opacity=".85"/>
{specks("#ffb27a", 71, 50, 100, 450, 2.4)}
{peaks(430, "#5a1c12", 72, hmin=30, hmax=80)}
{ridge(460, 16, "#3a100a", 73)}
<rect x="0" y="470" width="630" height="410" fill="#2a0c08"/>
{dead_tree(470, 470, 1.4)}{dead_tree(120, 476, .9)}
<g fill="{R}">{"".join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in [(230,486,9),(260,492,6),(380,488,8),(560,494,7),(60,496,6)])}</g>
<path d="M280 470 L292 430 Q300 410 320 412 L360 412 Q376 412 382 400 L392 386 L400 390 L402 402 Q396 410 392 418 Q388 430 380 436 L382 470 L374 470 L370 444 L300 444 L296 470Z" fill="{I}"/>
<circle cx="392" cy="398" r="2.5" fill="#ff5a3a"/>"""),
"08-chateau-orage": dict(s0="#2b2f38", s1="#7d7f86", sun="#e8e2cf", body=lambda: f"""
<g fill="#1e2128" opacity=".8"><ellipse cx="160" cy="140" rx="200" ry="50"/><ellipse cx="480" cy="120" rx="200" ry="56"/><ellipse cx="330" cy="200" rx="230" ry="40"/></g>
<path d="M470 110 L440 200 L462 204 L430 300" stroke="#ffe7a8" stroke-width="4" fill="none"/>
<path d="M-20 880 L-20 470 L120 440 L200 380 L260 360 L380 360 L440 390 L520 440 L650 460 L650 880Z" fill="#191b20"/>
{use("castle", 320, 362, 1.25, fill="#111317")}
<path d="M180 520 Q260 470 300 470" stroke="#3a3d45" stroke-width="10" fill="none"/>
{use("soldier", 200, 510, .55, fill="#111317")}
{rain(81)}"""),
"09-site-de-grace": dict(s0="#2a2016", s1="#5a4026", sun="#ffd98a", body=lambda: f"""
<g fill="#1a130c">
  <rect x="60" y="120" width="44" height="400"/><rect x="526" y="120" width="44" height="400"/>
  <path d="M40 120 H124 V100 H40Z M506 120 H590 V100 H506Z"/>
  <path d="M104 160 Q315 40 526 160 V130 Q315 20 104 130Z"/>
</g>
<circle cx="315" cy="420" r="200" fill="url(#sun)"/>
{specks("#ffe7a8", 91, 70, 200, 500, 2.6)}
<path d="M315 470 L300 340 L315 300 L330 340Z" fill="#fff1c4" opacity=".85"/>
<rect x="0" y="480" width="630" height="400" fill="#1a130c"/>
<path d="M222 480 L226 430 Q214 410 222 392 L246 376 Q262 372 266 384 L270 410 L282 430 L276 480Z" fill="{I}"/>
<circle cx="250" cy="366" r="12" fill="{I}"/>
<path d="M236 400 Q270 402 288 410" stroke="{I}" stroke-width="9" stroke-linecap="round"/>
<path d="M288 360 L292 350 L296 360 V480 H288Z" fill="{G}"/><rect x="280" y="368" width="24" height="5" fill="{I}"/>"""),
"10-montagnes": dict(s0="#a9b8c8", s1="#eef1f4", sun="#ffffff", body=lambda: f"""
<circle cx="200" cy="200" r="200" fill="url(#sun)"/>
{peaks(420, "#7d8a9a", 101, hmin=120, hmax=260, snow="#f7f9fb")}
<path d="M430 210 Q420 170 440 140 Q446 170 458 176 Q462 150 476 130 Q482 176 470 210Z" fill="#ff8a3a"/>
<path d="M444 210 Q440 186 450 170 Q456 190 462 192 Q466 180 470 172 Q472 196 464 210Z" fill="#ffd27a"/>
{peaks(470, "#9aa6b4", 102, hmin=60, hmax=140, snow="#ffffff")}
<rect x="0" y="470" width="630" height="410" fill="#e6ebf0"/>
<path d="M150 480 Q300 460 420 486" stroke="#c9d2dc" stroke-width="6" fill="none"/>
{use("warrior", 300, 488, 1.1)}
{specks("#ffffff", 103, 90, 90, 520, 2.4)}"""),
}

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("*.svg"):
        old.unlink()
    for name, sc in SCENES.items():
        head = HEAD.replace("{s0}", sc["s0"]).replace("{s1}", sc["s1"]).replace("{sun}", sc["sun"])
        (OUT / f"{name}.svg").write_text(head + sc["body"]() + FOOT, encoding="utf-8")
    print(f"{len(SCENES)} scènes écrites dans {OUT}")
