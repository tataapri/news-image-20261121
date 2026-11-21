#!/usr/bin/env python3
"""Draw the 21 November 2026 world-news front page (1024x1024 PNG).

Pure Pillow drawing: flat vector-style illustrations, no photos, no network.
Run: python3 draw_poster.py  ->  writes entry.png next to this file.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 246, 236)
INK = (24, 24, 28)
NAVY = (18, 38, 76)
RED = (178, 34, 34)
BLUE = (30, 80, 160)
GOLD = (198, 142, 26)
TEAL = (14, 110, 110)
GREEN = (34, 120, 60)
GREY = (90, 90, 96)
CARD = (255, 255, 255)
LINE = (200, 192, 176)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FSB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FSR = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap by pixel width."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, width, fill=INK, leading=None):
    lh = leading or int(fnt.size * 1.28)
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += lh
    return y


def kicker(draw, x, y, text, color):
    f = font(FB, 15)
    draw.text((x, y), text.upper(), font=f, fill=color)
    return y + 22


# ---------------------------------------------------------------- canvas
img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------------------------------------------------------------- masthead
d.rectangle([0, 0, W, 148], fill=NAVY)
d.text((512, 26), "THE WORLD TODAY", font=font(FSB, 62),
       fill=(255, 255, 255), anchor="ma")
d.text((512, 102), "SATURDAY, 21 NOVEMBER 2026  •  THE DAY IN ONE PAGE",
       font=font(FB, 25), fill=(255, 214, 90), anchor="ma")
d.rectangle([24, 156, W - 24, 159], fill=INK)

# ---------------------------------------------------------------- lead story
LX, LY, LW, LH = 24, 172, 976, 232
d.rectangle([LX, LY, LX + LW, LY + LH], fill=CARD, outline=LINE, width=2)
d.rectangle([LX, LY, LX + LW, LY + 6], fill=RED)

# lead illustration: night sky, radar arcs, missile streak, Polish flag
ix, iy, iw, ih = LX + 14, LY + 18, 300, LH - 36
d.rectangle([ix, iy, ix + iw, iy + ih], fill=(16, 28, 52))
for r in (34, 62, 90):
    d.arc([ix + 150 - r, iy + ih - r, ix + 150 + r, iy + ih + r],
          start=270, end=360, fill=(90, 160, 220), width=3)
d.line([ix + 150, iy + ih, ix + 150, iy + 40], fill=(90, 160, 220), width=2)
# missile streak
d.line([ix + 30, iy + 55, ix + 250, iy + 30], fill=(255, 200, 80), width=5)
d.polygon([(ix + 250, iy + 30), (ix + 232, iy + 22), (ix + 232, iy + 38)],
          fill=(255, 200, 80))
d.ellipse([ix + 22, iy + 47, ix + 38, iy + 63], fill=(255, 120, 60))
# Polish flag (white over red) bottom-left of the scene
d.rectangle([ix + 18, iy + ih - 52, ix + 98, iy + ih - 27], fill=(255, 255, 255))
d.rectangle([ix + 18, iy + ih - 27, ix + 98, iy + ih - 4], fill=(220, 20, 60))
d.text((ix + 112, iy + ih - 52), "POLAND", font=font(FB, 19), fill=(255, 255, 255))

tx = LX + 340
y = LY + 16
y = kicker(d, tx, y, "Lead story — Europe", RED)
d.text((tx, y), "Russian missiles land", font=font(FSB, 33), fill=INK)
y += 42
d.text((tx, y), "in Poland; NATO alerted", font=font(FSB, 33), fill=INK)
y += 46
para(d, tx, y,
     "Two missiles and a drone came down in Poland during a huge "
     "Russian attack on Ukraine. Warsaw calls it a deliberate "
     "provocation; NATO calls it a grave violation. Eight people "
     "were killed in Ukraine, and France seeks a UN meeting.",
     font(FR, 18), LW - 366 - 14, leading=24)

# ---------------------------------------------------------------- grid of six
stories = [
    dict(tag="Markets — USA", color=RED,
         head="Wall Street plunges",
         body="The S&P 500 slides into correction as the AI sell-off "
              "deepens. The Nasdaq falls 5.28% and Nvidia drops about 14%.",
         art="chart"),
    dict(tag="Europe — Denmark", color=NAVY,
         head="Denmark expels Russian envoy",
         body="Copenhagen expels Russia's defence attache over an alleged "
              "plot to kill Ukrainian rapper Kyivstoner at a concert.",
         art="flag"),
    dict(tag="Africa — South Africa", color=GREEN,
         head="ANC scrambles for coalitions",
         body="After its worst local-election result, 31%, the ANC holds "
              "the most votes in only two of eight big cities.",
         art="ballot"),
    dict(tag="USA — New York", color=TEAL,
         head="Mamdani: close Rikers by 2032",
         body="New York's mayor unveils a plan to shut the Rikers Island "
              "jail and open four borough jails, with $146m for care.",
         art="jail"),
    dict(tag="Tech — USA", color=BLUE,
         head="Waymo recalls its robotaxis",
         body="Alphabet's self-driving unit files two recalls after its "
              "cars entered closed freeway lanes and ignored traffic control.",
         art="car"),
    dict(tag="Middle East", color=GOLD,
         head="Missiles over Riyadh stopped",
         body="Saudi Arabia says it intercepted Houthi missiles over the "
              "capital, as its coalition strikes back at Hodeidah.",
         art="shield"),
]

GX, GY = 24, 420
CW, CH, GAP = 317, 268, 12

for i, s in enumerate(stories):
    cx = GX + (i % 3) * (CW + GAP)
    cy = GY + (i // 3) * (CH + GAP)
    d.rectangle([cx, cy, cx + CW, cy + CH], fill=CARD, outline=LINE, width=2)
    d.rectangle([cx, cy, cx + CW, cy + 5], fill=s["color"])

    # illustration band
    ax, ay, aw, ah = cx + 12, cy + 14, CW - 24, 92
    if s["art"] == "chart":
        d.rectangle([ax, ay, ax + aw, ay + ah], fill=(245, 230, 230))
        d.line([ax + 16, ay + 78, ax + 70, ay + 58, ax + 130, ay + 64,
                ax + 190, ay + 34, ax + 250, ay + 22, ax + 278, ay + 14],
               fill=RED, width=5)
        d.polygon([(ax + 278, ay + 14), (ax + 262, ay + 10), (ax + 268, ay + 28)],
                  fill=RED)
        for gx in (ax + 16, ax + 86, ax + 156, ax + 226):
            d.line([gx, ay + ah - 6, gx, ay + ah - 12], fill=GREY, width=2)
        d.text((ax + 16, ay + 8), "-5.28%", font=font(FB, 22), fill=RED)
    elif s["art"] == "flag":
        d.rectangle([ax, ay, ax + aw, ay + ah], fill=(200, 30, 50))
        d.rectangle([ax + 92, ay, ax + 118, ay + ah], fill=(255, 255, 255))
        d.rectangle([ax, ay + 34, ax + aw, ay + 58], fill=(255, 255, 255))
        d.text((ax + 150, ay + 30), "COPENHAGEN", font=font(FB, 17),
               fill=(255, 255, 255))
    elif s["art"] == "ballot":
        d.rectangle([ax, ay, ax + aw, ay + ah], fill=(232, 240, 232))
        d.rectangle([ax + 96, ay + 34, ax + 198, ay + ah - 8], fill=(40, 60, 120))
        d.rectangle([ax + 96, ay + 34, ax + 198, ay + 48], fill=(40, 60, 120))
        d.rectangle([ax + 130, ay + 22, ax + 164, ay + 36], fill=(255, 255, 255),
                    outline=INK, width=2)
        d.line([ax + 136, ay + 30, ax + 146, ay + 40, ax + 158, ay + 22],
               fill=GREEN, width=4)
        d.text((ax + 208, ay + 44), "31%", font=font(FB, 26), fill=INK)
        d.text((ax + 16, ay + 44), "VOTE", font=font(FB, 20), fill=GREY)
    elif s["art"] == "jail":
        d.rectangle([ax, ay, ax + aw, ay + ah], fill=(210, 222, 235))
        for bx in range(ax + 20, ax + aw - 10, 34):
            d.rectangle([bx, ay + 8, bx + 12, ay + 52], fill=(40, 50, 70))
        d.rectangle([ax, ay + 40, ax + aw, ay + 50], fill=(40, 50, 70))
        d.rectangle([ax, ay + 58, ax + aw, ay + ah], fill=(255, 255, 255))
        d.text((ax + 16, ay + 64), "RIKERS  •  2032", font=font(FB, 17), fill=NAVY)
    elif s["art"] == "car":
        d.rectangle([ax, ay, ax + aw, ay + ah], fill=(228, 238, 248))
        d.ellipse([ax + 60, ay + 52, ax + 92, ay + 84], fill=INK)
        d.ellipse([ax + 200, ay + 52, ax + 232, ay + 84], fill=INK)
        d.rounded_rectangle([ax + 44, ay + 30, ax + 248, ay + 58],
                            radius=12, fill=(30, 110, 180))
        d.polygon([(ax + 96, ay + 30), (ax + 130, ay + 8), (ax + 190, ay + 8),
                   (ax + 210, ay + 30)], fill=(120, 180, 230))
        d.line([ax + 146, ay + 8, ax + 146, ay - 2], fill=INK, width=3)
        d.ellipse([ax + 140, ay - 8, ax + 152, ay + 4], fill=RED)
        d.polygon([(ax + 252, ay + 12), (ax + 272, ay + 46), (ax + 232, ay + 46)],
                  fill=(255, 200, 40), outline=INK)
        d.text((ax + 246, ay + 24), "!", font=font(FB, 18), fill=INK)
    elif s["art"] == "shield":
        d.rectangle([ax, ay, ax + aw, ay + ah], fill=(24, 40, 60))
        for mx, my in ((ax + 60, ay + 20), (ax + 150, ay + 12), (ax + 230, ay + 24)):
            d.line([mx, my, mx - 14, my + 26], fill=(255, 200, 80), width=3)
            d.ellipse([mx - 18, my + 22, mx - 10, my + 30], fill=(255, 120, 60))
        d.polygon([(ax + 146, ay + 34), (ax + 186, ay + 46), (ax + 186, ay + 66),
                   (ax + 146, ay + 86), (ax + 106, ay + 66), (ax + 106, ay + 46)],
                  fill=(40, 140, 160), outline=(255, 255, 255), width=3)
        d.text((ax + 138, ay + 50), "✓", font=font(FB, 26), fill=(255, 255, 255))

    y = cy + 116
    y = kicker(d, cx + 14, y, s["tag"], s["color"])
    y = para(d, cx + 14, y, s["head"], font(FSB, 22), CW - 28, leading=27)
    para(d, cx + 14, y + 4, s["body"], font(FR, 15), CW - 28, leading=20)

# ---------------------------------------------------------------- footer
d.rectangle([24, 972, W - 24, 975], fill=INK)
d.text((512, 982),
       "Sources: AP, Reuters, Al Jazeera, BBC, City of New York  •  All stories reported on 21 November 2026",
       font=font(FR, 15), fill=GREY, anchor="ma")

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
