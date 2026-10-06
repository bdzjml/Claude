"""Génère les 20 illustrations SVG des cartes (gravure dorée sur parchemin, 630x880)."""
from pathlib import Path

I, G, R, B, CLAY = "#2a1d12", "#b8892e", "#8e2a1e", "#3f6c9e", "#8a5a3a"
OUT = Path(__file__).resolve().parent.parent / "illustrations"

HEAD = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 630 880" width="630" height="880">
<defs>
  <linearGradient id="parch" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#eadfc4"/><stop offset="1" stop-color="#c9b38a"/>
  </linearGradient>
  <radialGradient id="vig" cx=".5" cy=".42" r=".75">
    <stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#3a2410" stop-opacity=".55"/>
  </radialGradient>
  <radialGradient id="halo" cx=".5" cy=".5" r=".5">
    <stop offset="0" stop-color="{G}" stop-opacity=".55"/><stop offset="1" stop-color="{G}" stop-opacity="0"/>
  </radialGradient>
  <pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(35)">
    <line x1="0" y1="0" x2="0" y2="7" stroke="{I}" stroke-width="1.6"/>
  </pattern>
  <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="7"/>
    <feColorMatrix values="0 0 0 0 .2  0 0 0 0 .13  0 0 0 0 .05  0 0 0 .16 0"/></filter>
</defs>
<rect width="630" height="880" fill="url(#parch)"/>
<rect width="630" height="880" filter="url(#grain)"/>
<circle cx="315" cy="300" r="230" fill="url(#halo)"/>
"""

FOOT = f"""<path d="M0 560 Q160 520 315 545 Q470 570 630 530 V880 H0Z" fill="url(#hatch)" opacity=".55"/>
<rect width="630" height="880" fill="url(#vig)"/>
<rect x="24" y="24" width="582" height="832" rx="16" fill="none" stroke="{I}" stroke-width="4"/>
<rect x="36" y="36" width="558" height="808" rx="12" fill="none" stroke="{G}" stroke-width="3"/>
<g fill="{G}" stroke="{I}" stroke-width="2">
  <path d="M36 70 L70 36 L80 46 L46 80Z"/><path d="M594 70 L560 36 L550 46 L584 80Z"/>
  <path d="M36 810 L70 844 L80 834 L46 800Z"/><path d="M594 810 L560 844 L550 834 L584 800Z"/>
</g>
</svg>
"""

def rays(cx=315, cy=300, n=24, r1=150, r2=250):
    import math
    out = []
    for k in range(n):
        a = 2 * math.pi * k / n
        out.append(f'<line x1="{cx + r1 * math.cos(a):.0f}" y1="{cy + r1 * math.sin(a):.0f}" '
                   f'x2="{cx + r2 * math.cos(a):.0f}" y2="{cy + r2 * math.sin(a):.0f}"/>')
    return f'<g stroke="{G}" stroke-width="2" opacity=".6">{"".join(out)}</g>'

def stars(points):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{G}"/>' for x, y, r in points)

SUBJECTS = {
"01-chevalier": rays() + f"""
<path d="M262 270 Q230 420 215 520 L415 520 Q400 420 368 270Z" fill="{R}"/>
<path d="M268 262 Q315 245 362 262 L378 380 L345 392 L340 520 L318 520 L315 420 L312 520 L290 520 L285 392 L252 380Z" fill="{I}"/>
<path d="M285 300 H345 M282 330 H348 M280 360 H350" stroke="{G}" stroke-width="3"/>
<path d="M318 172 C330 140 365 128 392 140 C365 146 345 160 332 178Z" fill="{R}"/>
<path d="M315 172 C290 172 280 192 280 214 L280 248 Q282 262 296 264 L334 264 Q348 262 350 248 L350 214 C350 192 340 172 315 172Z" fill="{I}"/>
<rect x="292" y="212" width="46" height="6" fill="{G}"/>
<ellipse cx="262" cy="272" rx="24" ry="16" fill="{I}" stroke="{G}" stroke-width="3"/>
<ellipse cx="368" cy="272" rx="24" ry="16" fill="{I}" stroke="{G}" stroke-width="3"/>
<path d="M362 270 L392 350 L404 345 L376 262Z" fill="{I}"/>
<path d="M392 120 L397 98 L402 120 L404 330 L390 330Z" fill="{G}" stroke="{I}" stroke-width="2"/>
<rect x="374" y="330" width="46" height="10" rx="3" fill="{I}" stroke="{G}" stroke-width="2"/>
<rect x="391" y="340" width="12" height="40" fill="{I}"/><circle cx="397" cy="386" r="8" fill="{G}"/>
<path d="M190 300 H275 V365 Q275 420 232 445 Q190 420 190 365Z" fill="{I}" stroke="{G}" stroke-width="6"/>
<path d="M232 425 V330 M232 360 L212 340 M232 360 L252 340 M232 385 L208 368 M232 385 L256 368" stroke="{G}" stroke-width="5" fill="none" stroke-linecap="round"/>
""",
"02-dragon": f"""
<path d="M120 180 L240 300 M510 180 L390 300" stroke="{I}" stroke-width="3"/>
<path d="M315 300 L150 150 L175 230 L115 222 L170 290 L105 305 L200 345Z" fill="{I}"/>
<path d="M315 300 L480 150 L455 230 L515 222 L460 290 L525 305 L430 345Z" fill="{I}"/>
<path d="M315 300 L150 150 M315 300 L115 222 M315 300 L105 305 M315 300 L480 150 M315 300 L515 222 M315 300 L525 305" stroke="{G}" stroke-width="2.5"/>
<path d="M300 470 Q240 520 180 500 Q150 490 135 508 Q170 524 192 527 Q262 532 322 480Z" fill="{I}"/>
<path d="M255 330 Q315 290 375 330 Q395 400 350 460 Q315 490 280 460 Q235 400 255 330Z" fill="{I}"/>
<path d="M255 330 Q315 290 375 330 Q395 400 350 460 Q315 490 280 460 Q235 400 255 330Z" fill="url(#hatch)" opacity=".5"/>
<path d="M300 320 Q290 260 315 220 Q340 190 360 200 L392 195 L374 212 L382 222 L352 226 Q335 240 332 270 Q330 300 330 320Z" fill="{I}"/>
<path d="M340 198 L328 166 L350 192Z M352 196 L358 164 L364 196Z" fill="{I}"/>
<circle cx="352" cy="207" r="4" fill="{G}"/>
<path d="M394 200 L432 188 L420 206 L466 194 L448 214 L490 208" stroke="{G}" stroke-width="5" fill="none" stroke-linejoin="round"/>
<path d="M270 470 L262 520 M360 470 L370 520" stroke="{I}" stroke-width="16" stroke-linecap="round"/>
""",
"03-sorcier": f"""
<path d="M400 140 A90 90 0 1 0 400 330 A70 70 0 1 1 400 140Z" fill="{G}" opacity=".85"/>
{stars([(170,150,3),(205,210,2),(470,120,3),(500,260,2),(150,300,2),(480,360,3),(230,120,2)])}
<path d="M315 205 Q280 210 268 260 L225 520 L405 520 L362 260 Q350 210 315 205Z" fill="{I}"/>
<path d="M268 260 L225 520 M362 260 L405 520" stroke="{G}" stroke-width="4"/>
<circle cx="315" cy="380" r="26" fill="none" stroke="{G}" stroke-width="3"/>
<path d="M315 354 V406 M289 380 H341" stroke="{G}" stroke-width="2"/>
<path d="M315 160 Q275 165 272 215 Q280 250 315 255 Q350 250 358 215 Q355 165 315 160Z" fill="{I}"/>
<ellipse cx="315" cy="222" rx="22" ry="26" fill="#000"/>
<circle cx="306" cy="220" r="3.5" fill="#8fc0ee"/><circle cx="324" cy="220" r="3.5" fill="#8fc0ee"/>
<path d="M352 290 Q380 300 400 296 L402 310 Q375 316 348 310Z" fill="{I}"/>
<rect x="398" y="160" width="8" height="360" fill="{I}"/>
<path d="M402 112 L420 146 L402 176 L384 146Z" fill="{B}" stroke="{G}" stroke-width="3"/>
<circle cx="402" cy="146" r="40" fill="{B}" opacity=".18"/>
""",
"04-loup": f"""
<circle cx="315" cy="235" r="120" fill="{G}" opacity=".8"/>
<circle cx="280" cy="210" r="16" fill="{I}" opacity=".12"/><circle cx="345" cy="265" r="22" fill="{I}" opacity=".1"/>
<path d="M250 520 L262 420 Q250 380 270 340 Q285 300 300 285 L296 250 Q300 225 318 205 L330 160 L338 200 L350 188 L352 214 Q372 222 394 212 L400 224 Q380 240 362 244 Q350 262 352 290 Q372 330 380 380 Q392 440 400 520 L372 520 L364 452 Q340 470 320 470 L316 520Z" fill="{I}"/>
<path d="M380 470 Q445 482 455 428 Q442 466 400 440Z" fill="{I}"/>
<circle cx="340" cy="216" r="3.5" fill="{G}"/>
<path d="M300 300 Q320 340 318 400 M330 300 Q350 350 352 410" stroke="{G}" stroke-width="2" opacity=".6" fill="none"/>
""",
"05-ours": rays(n=18) + f"""
<path d="M258 300 Q215 260 200 210 L214 205 Q232 250 268 280Z" fill="{R}" stroke="{I}" stroke-width="5"/>
<path d="M372 300 Q415 260 430 210 L416 205 Q398 250 362 280Z" fill="{R}" stroke="{I}" stroke-width="5"/>
<path d="M196 208 L186 190 M204 204 L198 184 M212 204 L210 184 M434 208 L444 190 M426 204 L432 184 M418 204 L420 184" stroke="{G}" stroke-width="4" stroke-linecap="round"/>
<path d="M250 520 L262 430 Q235 380 245 320 Q252 280 280 262 Q270 240 280 225 Q290 205 315 200 Q340 205 350 225 Q360 240 350 262 Q378 280 385 320 Q395 380 368 430 L380 520 L342 520 L334 460 L296 460 L288 520Z" fill="{R}" stroke="{I}" stroke-width="6"/>
<path d="M262 330 Q315 300 368 330 M258 370 Q315 345 372 370 M262 410 Q315 390 368 410" stroke="{I}" stroke-width="2.5" fill="none" opacity=".7"/>
<circle cx="288" cy="212" r="12" fill="{R}" stroke="{I}" stroke-width="5"/><circle cx="342" cy="212" r="12" fill="{R}" stroke="{I}" stroke-width="5"/>
<ellipse cx="315" cy="250" rx="15" ry="11" fill="{I}"/>
<circle cx="302" cy="232" r="4" fill="{G}"/><circle cx="328" cy="232" r="4" fill="{G}"/>
""",
"06-serpent": f"""
<path d="M180 540 Q200 470 230 520 Q250 450 280 530 Q300 470 330 535 Q350 460 380 530 Q400 470 430 540Z" fill="{R}" opacity=".85"/>
<path d="M230 540 Q250 500 270 535 Q290 495 315 538 Q340 500 360 536Z" fill="{G}"/>
<path d="M200 500 Q160 420 260 400 Q380 380 370 320 Q360 260 280 270 Q220 280 240 220 Q260 170 330 170" stroke="{I}" stroke-width="46" fill="none" stroke-linecap="round"/>
<path d="M200 500 Q160 420 260 400 Q380 380 370 320 Q360 260 280 270 Q220 280 240 220 Q260 170 330 170" stroke="{G}" stroke-width="6" fill="none" stroke-dasharray="4 14"/>
<path d="M318 148 Q372 136 404 164 Q382 194 326 194Z" fill="{I}"/>
<circle cx="372" cy="160" r="5" fill="{R}"/>
<path d="M402 168 L432 172 L444 162 M432 172 L444 182" stroke="{R}" stroke-width="3" fill="none"/>
""",
"07-arbre": rays(cy=240, n=32, r1=120, r2=270) + f"""
<g fill="{G}" opacity=".92">
  <circle cx="315" cy="200" r="70"/><circle cx="250" cy="230" r="52"/><circle cx="380" cy="230" r="52"/>
  <circle cx="275" cy="165" r="44"/><circle cx="355" cy="165" r="44"/><circle cx="315" cy="135" r="40"/>
  <circle cx="210" cy="270" r="36"/><circle cx="420" cy="270" r="36"/>
</g>
<g stroke="{I}" stroke-width="2" opacity=".35" fill="none">
  <path d="M260 210 Q290 200 300 230 M340 190 Q360 170 380 200 M290 150 Q310 130 330 150"/>
</g>
<path d="M300 520 Q305 420 296 360 Q290 320 315 280 Q340 320 334 360 Q325 420 330 520Z" fill="{G}" stroke="{I}" stroke-width="4"/>
<path d="M310 300 Q270 280 240 250 M318 300 Q360 270 392 250 M312 330 Q270 320 220 290 M320 330 Q370 320 410 290" stroke="{G}" stroke-width="9" fill="none" stroke-linecap="round"/>
<path d="M305 520 Q260 500 200 515 M325 520 Q370 500 430 515" stroke="{G}" stroke-width="6" fill="none"/>
<path d="M222 520 L226 486 Q218 470 230 460 Q244 456 246 470 L250 486 L262 500 L256 520Z" fill="{I}"/>
<circle cx="236" cy="452" r="9" fill="{I}"/>
""",
"08-astres": f"""
<circle cx="315" cy="255" r="170" fill="{I}"/>
<circle cx="315" cy="255" r="170" fill="none" stroke="{G}" stroke-width="4"/>
{stars([(230,180,2.5),(260,240,1.5),(400,200,2.5),(420,320,1.5),(210,330,2),(350,150,1.5),(300,370,2),(370,380,2.5),(180,250,1.5),(450,250,2),(330,230,1.5),(270,320,1.5)])}
<g stroke="{G}" stroke-linecap="round">
  <path d="M190 140 L300 250" stroke-width="3" opacity=".7"/><circle cx="300" cy="250" r="9" fill="{G}"/>
  <path d="M330 110 L400 260" stroke-width="3" opacity=".7"/><circle cx="400" cy="260" r="11" fill="{G}"/>
  <path d="M440 150 L470 230" stroke-width="2" opacity=".7"/><circle cx="470" cy="230" r="6" fill="{G}"/>
</g>
<circle cx="250" cy="370" r="32" fill="#6b4a8a" opacity=".7"/>
<ellipse cx="250" cy="370" rx="58" ry="10" fill="none" stroke="{G}" stroke-width="3"/>
<path d="M300 545 L306 485 L282 445 L292 439 L312 467 L318 467 L338 439 L348 445 L324 485 L330 545Z" fill="{I}"/>
<circle cx="315" cy="456" r="13" fill="{I}"/>
""",
"09-fleur": f"""
<path d="M315 520 Q300 440 318 360" stroke="{I}" stroke-width="12" fill="none"/>
<path d="M310 450 Q260 430 240 400 Q285 405 312 440Z M318 420 Q370 400 392 370 Q345 372 318 410Z" fill="{I}"/>
<g fill="{R}" stroke="{I}" stroke-width="4">
  <ellipse cx="315" cy="220" rx="40" ry="95"/>
  <ellipse cx="315" cy="270" rx="40" ry="95" transform="rotate(60 315 270)"/>
  <ellipse cx="315" cy="270" rx="40" ry="95" transform="rotate(-60 315 270)"/>
  <ellipse cx="315" cy="300" rx="34" ry="70" transform="rotate(180 315 300)"/>
</g>
<circle cx="315" cy="275" r="38" fill="{I}"/>
<circle cx="315" cy="275" r="22" fill="{G}"/>
{stars([(300,268,3),(326,282,3),(318,262,2)])}
<g fill="{R}" stroke="{I}" stroke-width="2">
  <path d="M160 180 Q140 160 150 150 Q170 160 168 180 Q190 160 200 170 Q190 190 168 186Z"/>
  <path d="M460 160 Q440 140 450 130 Q470 140 468 160 Q490 140 500 150 Q490 170 468 166Z"/>
  <path d="M470 380 Q450 360 460 350 Q480 360 478 380 Q500 360 510 370 Q500 390 478 386Z"/>
  <path d="M150 400 Q130 380 140 370 Q160 380 158 400 Q180 380 190 390 Q180 410 158 406Z"/>
</g>
{stars([(200,250,3),(430,220,3),(220,320,2),(420,330,2),(250,140,2),(380,130,2)])}
""",
"10-assassin": f"""
<g stroke="{I}" stroke-width="3" opacity=".35" fill="none">
  <path d="M220 200 Q180 260 200 330 M410 210 Q450 270 430 340 M240 160 Q200 190 190 240"/>
</g>
<path d="M315 170 Q265 175 258 240 Q240 330 205 520 L425 520 Q390 330 372 240 Q365 175 315 170Z" fill="{I}"/>
<path d="M258 240 Q240 330 205 520" stroke="#7a5aa6" stroke-width="5" fill="none"/>
<path d="M372 240 Q390 330 425 520" stroke="#7a5aa6" stroke-width="5" fill="none"/>
<path d="M315 205 Q290 210 288 245 Q300 268 315 270 Q330 268 342 245 Q340 210 315 205Z" fill="#000"/>
<path d="M300 236 L310 240 M320 240 L330 236" stroke="{R}" stroke-width="4" stroke-linecap="round"/>
<path d="M360 300 Q400 280 420 250 L432 258 Q414 292 368 320Z" fill="{I}"/>
<path d="M425 252 L472 186 L478 192 L433 258Z" fill="{G}" stroke="{I}" stroke-width="2"/>
<path d="M418 248 L440 266" stroke="{I}" stroke-width="6"/>
<path d="M472 186 L500 160" stroke="{G}" stroke-width="2" opacity=".6"/>
""",
"11-roi-dechu": rays(cy=150, n=20, r1=60, r2=150) + f"""
<path d="M255 180 L275 128 L295 168 L315 116 L335 168 L355 128 L375 180Z" fill="{G}" stroke="{I}" stroke-width="4"/>
<circle cx="275" cy="128" r="6" fill="{R}"/><circle cx="315" cy="116" r="6" fill="{R}"/><circle cx="355" cy="128" r="6" fill="{R}"/>
<path d="M316 118 L308 146 L322 156 L312 180" stroke="{I}" stroke-width="5" fill="none"/>
<path d="M260 520 Q262 420 285 360 Q290 320 315 300 Q340 320 345 360 Q368 420 370 520Z" fill="{I}"/>
<path d="M260 520 Q262 420 285 360 M370 520 Q368 420 345 360" stroke="{G}" stroke-width="3" fill="none"/>
<circle cx="315" cy="288" r="22" fill="{I}"/>
<path d="M300 276 Q288 252 298 236 Q302 258 310 268Z M330 276 Q342 252 332 236 Q328 258 320 268Z" fill="{I}"/>
<path d="M392 330 L398 312 L404 330 V520 H392Z" fill="{G}" stroke="{I}" stroke-width="2"/>
<rect x="374" y="330" width="48" height="10" rx="3" fill="{I}" stroke="{G}" stroke-width="2"/>
<path d="M345 380 Q370 360 392 350" stroke="{I}" stroke-width="14" stroke-linecap="round"/>
""",
"12-flamme": f"""
<path d="M315 110 C350 160 410 180 392 252 C384 296 346 318 315 320 C284 318 246 296 238 252 C220 180 280 160 315 110Z" fill="{R}"/>
<path d="M315 160 C335 195 370 210 360 255 C354 282 334 296 315 297 C296 296 276 282 270 255 C260 210 295 195 315 160Z" fill="{G}"/>
<path d="M315 215 C325 235 342 245 336 268 C332 282 322 288 315 288 C308 288 298 282 294 268 C288 245 305 235 315 215Z" fill="#f3e3b5"/>
<path d="M200 200 Q215 170 210 140 M430 200 Q415 170 420 140 M180 300 Q200 270 190 240 M450 300 Q430 270 440 240" stroke="{R}" stroke-width="4" fill="none" opacity=".6"/>
<path d="M286 520 L292 410 Q280 372 290 352 L250 326 L258 312 L300 334 Q315 326 330 334 L372 312 L380 326 L340 352 Q350 372 338 410 L344 520Z" fill="{I}"/>
<circle cx="315" cy="346" r="18" fill="{I}"/>
""",
"13-sang": f"""
<path d="M200 520 V170" stroke="{I}" stroke-width="10"/>
<path d="M176 175 V120 L182 108 L188 120 V160 H212 V120 L218 108 L224 120 V175Z" fill="{I}"/>
<path d="M194 160 V100 L200 86 L206 100 V160Z" fill="{I}"/>
<path d="M245 230 H385 Q380 310 315 330 Q250 310 245 230Z" fill="{G}" stroke="{I}" stroke-width="5"/>
<path d="M250 232 H380 Q376 246 360 250 Q356 290 350 302 Q346 262 330 252 Q320 300 314 312 Q310 262 296 252 Q286 280 282 292 Q278 256 262 250 Q252 246 250 232Z" fill="{R}"/>
<ellipse cx="315" cy="232" rx="70" ry="10" fill="{R}" stroke="{I}" stroke-width="4"/>
<rect x="306" y="330" width="18" height="80" fill="{G}" stroke="{I}" stroke-width="4"/>
<path d="M258 432 Q315 400 372 432 L372 448 H258Z" fill="{G}" stroke="{I}" stroke-width="4"/>
<path d="M350 448 Q352 480 346 500 Q340 480 342 448Z M290 448 Q292 470 286 486 Q280 470 282 448Z" fill="{R}"/>
<path d="M230 520 Q315 500 420 520" stroke="{R}" stroke-width="10" fill="none" opacity=".8"/>
""",
"14-doigts": f"""
<g fill="{I}" stroke="{G}" stroke-width="3">
  <rect x="200" y="160" width="34" height="210" rx="17" transform="rotate(-28 315 420)"/>
  <rect x="252" y="110" width="34" height="250" rx="17" transform="rotate(-10 315 420)"/>
  <rect x="300" y="95" width="34" height="265" rx="17" transform="rotate(4 315 420)"/>
  <rect x="348" y="115" width="34" height="245" rx="17" transform="rotate(16 315 420)"/>
  <rect x="380" y="240" width="34" height="170" rx="17" transform="rotate(48 315 420)"/>
  <path d="M230 360 Q228 470 290 520 L345 520 Q405 470 400 360Z"/>
</g>
<path d="M265 420 Q315 380 365 420 Q315 460 265 420Z" fill="{G}" stroke="{I}" stroke-width="3"/>
<circle cx="315" cy="420" r="16" fill="{I}"/><circle cx="320" cy="415" r="5" fill="#f3e3b5"/>
<g>
  <rect x="140" y="440" width="24" height="80" fill="#e9dcc0" stroke="{I}" stroke-width="3"/>
  <path d="M152 440 Q140 420 152 400 Q164 420 152 440Z" fill="{G}"/>
  <rect x="466" y="460" width="24" height="60" fill="#e9dcc0" stroke="{I}" stroke-width="3"/>
  <path d="M478 460 Q466 440 478 420 Q490 440 478 460Z" fill="{G}"/>
</g>
""",
"15-lame": f"""
<g fill="{R}" opacity=".75">
  <path d="M290 420 Q250 360 285 300 Q270 250 300 200 Q290 260 305 300 Q285 360 300 420Z"/>
  <path d="M340 420 Q380 360 345 300 Q360 250 330 200 Q340 260 325 300 Q345 360 330 420Z"/>
  <path d="M300 180 Q280 140 305 110 Q300 140 312 165Z"/>
</g>
<path d="M300 140 L315 100 L330 140 L326 430 L304 430Z" fill="{I}"/>
<path d="M315 150 V420" stroke="#4a3a2a" stroke-width="2"/>
<g fill="{G}"><circle cx="315" cy="180" r="4"/><rect x="312" y="210" width="6" height="16"/><circle cx="315" cy="250" r="4"/><rect x="312" y="280" width="6" height="16"/><circle cx="315" cy="320" r="4"/><rect x="312" y="350" width="6" height="16"/></g>
<path d="M240 430 Q315 412 390 430 L390 448 Q315 432 240 448Z" fill="{G}" stroke="{I}" stroke-width="3"/>
<rect x="305" y="448" width="20" height="62" fill="{I}"/>
<path d="M305 460 H325 M305 475 H325 M305 490 H325" stroke="{G}" stroke-width="2"/>
<circle cx="315" cy="520" r="13" fill="{G}" stroke="{I}" stroke-width="3"/>
""",
"16-archer": rays(cx=420, cy=200, n=16, r1=50, r2=120) + f"""
<path d="M200 170 Q130 320 200 470" stroke="{G}" stroke-width="9" fill="none" stroke-linecap="round"/>
<path d="M200 170 Q130 320 200 470" stroke="{I}" stroke-width="2" fill="none"/>
<path d="M200 170 L330 320 L200 470" stroke="{I}" stroke-width="2" fill="none"/>
<path d="M330 320 H150" stroke="{I}" stroke-width="4"/>
<path d="M150 320 L170 310 L170 330Z" fill="{G}"/>
<path d="M330 314 L345 306 M330 326 L345 334" stroke="{R}" stroke-width="4"/>
<path d="M340 520 L344 420 Q330 380 336 330 Q340 290 360 272 Q380 290 386 330 Q392 380 378 420 L384 520Z" fill="{I}"/>
<circle cx="360" cy="252" r="22" fill="{I}"/>
<path d="M338 250 Q350 220 372 226 Q390 236 384 258Z" fill="#e9dcc0" opacity=".25"/>
<path d="M352 300 Q300 316 230 320 L230 330 Q300 330 356 318Z" fill="{I}"/>
<path d="M366 300 Q350 318 330 322" stroke="{I}" stroke-width="12" stroke-linecap="round"/>
""",
"17-jarre": rays(n=18) + f"""
<path d="M260 440 L250 520 M370 440 L380 520" stroke="{I}" stroke-width="26" stroke-linecap="round"/>
<path d="M240 300 Q190 330 175 400 M390 300 Q440 330 455 400" stroke="{I}" stroke-width="24" stroke-linecap="round" fill="none"/>
<path d="M240 250 Q215 330 242 420 Q268 476 315 476 Q362 476 388 420 Q415 330 390 250Z" fill="{CLAY}" stroke="{I}" stroke-width="6"/>
<path d="M240 250 Q215 330 242 420 Q268 476 315 476 Q362 476 388 420 Q415 330 390 250Z" fill="url(#hatch)" opacity=".35"/>
<path d="M272 200 H358 L350 252 H280Z" fill="{CLAY}" stroke="{I}" stroke-width="6"/>
<ellipse cx="315" cy="200" rx="50" ry="12" fill="{I}"/>
<path d="M232 320 Q315 300 398 320 M228 380 Q315 362 402 380" stroke="#e9dcc0" stroke-width="10" fill="none" opacity=".8"/>
<circle cx="315" cy="350" r="34" fill="none" stroke="{G}" stroke-width="4"/>
<path d="M315 316 V384 M281 350 H349" stroke="{G}" stroke-width="3"/>
""",
"18-chateau": f"""
<circle cx="440" cy="170" r="50" fill="{G}" opacity=".85"/>
<path d="M150 150 Q160 140 170 150 Q180 140 190 150 M200 120 Q208 112 216 120 Q224 112 232 120" stroke="{I}" stroke-width="3" fill="none"/>
<path d="M120 520 L120 330 H140 V310 H160 V330 H180 V310 H200 V330 H215 V520Z" fill="{I}"/>
<path d="M415 520 L415 330 H430 V310 H450 V330 H470 V310 H490 V330 H510 V520Z" fill="{I}"/>
<path d="M215 520 V380 H235 V362 H255 V380 H275 V362 H295 V380 H335 V362 H355 V380 H375 V362 H395 V380 H415 V520Z" fill="{I}"/>
<path d="M270 380 V220 H285 V200 H300 V220 H330 V200 H345 V220 H360 V380Z" fill="{I}"/>
<path d="M265 222 L315 150 L365 222Z" fill="{I}"/>
<path d="M315 150 V110" stroke="{I}" stroke-width="4"/><path d="M315 110 L360 122 L315 134Z" fill="{R}"/>
<path d="M290 520 V470 Q315 440 340 470 V520Z" fill="{G}"/>
<g fill="{G}"><rect x="305" y="260" width="20" height="34" rx="10"/><rect x="155" y="380" width="14" height="24" rx="7"/><rect x="455" y="380" width="14" height="24" rx="7"/></g>
""",
"19-greffe": rays(n=24) + f"""
<g stroke="{I}" stroke-width="20" stroke-linecap="round" fill="none">
  <path d="M290 300 Q220 250 190 180"/><path d="M340 300 Q410 250 440 180"/>
  <path d="M280 340 Q200 330 150 280"/><path d="M350 340 Q430 330 480 280"/>
  <path d="M285 380 Q210 400 170 440"/><path d="M345 380 Q420 400 460 440"/>
</g>
<g fill="{G}" stroke="{I}" stroke-width="2">
  <path d="M182 172 L170 120 L196 166Z"/><path d="M448 172 L460 120 L434 166Z"/>
  <path d="M142 272 L108 236 L154 262Z"/><path d="M488 272 L522 236 L476 262Z"/>
  <circle cx="166" cy="446" r="16"/><circle cx="464" cy="446" r="16"/>
</g>
<ellipse cx="315" cy="360" rx="62" ry="100" fill="{I}"/>
<path d="M270 330 Q315 316 360 330 M268 370 Q315 356 362 370 M272 410 Q315 398 358 410" stroke="{G}" stroke-width="3" fill="none" stroke-dasharray="6 6"/>
<path d="M290 460 L282 520 M340 460 L348 520" stroke="{I}" stroke-width="22" stroke-linecap="round"/>
<circle cx="315" cy="245" r="32" fill="{I}"/>
<path d="M290 222 L300 196 L310 216 L320 192 L330 216 L340 196 L344 224Z" fill="{G}" stroke="{I}" stroke-width="2"/>
<circle cx="304" cy="248" r="4" fill="{G}"/><circle cx="326" cy="248" r="4" fill="{G}"/>
""",
"20-tome": rays(cy=220, n=24, r1=70, r2=170) + f"""
<g fill="none" stroke="{G}" stroke-width="3" opacity=".8">
  <circle cx="200" cy="200" r="20"/><path d="M200 180 V220 M180 200 H220"/>
  <circle cx="440" cy="180" r="18"/><path d="M428 168 L452 192 M452 168 L428 192"/>
  <path d="M315 120 L330 150 L300 150Z"/>
</g>
<path d="M260 520 L280 400 H350 L370 520Z" fill="{I}"/>
<path d="M200 330 L315 360 L430 330 L440 400 L315 420 L190 400Z" fill="{I}"/>
<path d="M210 320 Q262 300 312 330 V408 Q262 384 210 396Z" fill="#efe4c8" stroke="{I}" stroke-width="3"/>
<path d="M420 320 Q368 300 318 330 V408 Q368 384 420 396Z" fill="#efe4c8" stroke="{I}" stroke-width="3"/>
<g stroke="{I}" stroke-width="2" opacity=".7">
  <path d="M226 336 Q262 324 298 342 M226 352 Q262 340 298 358 M226 368 Q262 356 298 374"/>
  <path d="M334 342 Q368 324 404 336 M334 358 Q368 340 404 352 M334 374 Q368 356 404 368"/>
</g>
<rect x="232" y="340" width="20" height="22" fill="{R}" opacity=".8"/>
<rect x="452" y="290" width="22" height="70" fill="#efe4c8" stroke="{I}" stroke-width="3"/>
<path d="M463 290 Q450 268 463 248 Q476 268 463 290Z" fill="{G}"/>
<path d="M160 300 Q200 250 260 240" stroke="{I}" stroke-width="3" fill="none"/>
<path d="M160 300 Q170 270 196 262 Q186 284 160 300Z" fill="#efe4c8" stroke="{I}" stroke-width="2"/>
""",
}

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for name, body in SUBJECTS.items():
        (OUT / f"{name}.svg").write_text(HEAD + body + FOOT, encoding="utf-8")
    print(f"{len(SUBJECTS)} illustrations écrites dans {OUT}")
