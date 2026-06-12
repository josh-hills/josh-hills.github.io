"""Generate the Open Graph preview image (assets/og.png).

Run from the repo root: ``python3 scripts/make_og.py``. Requires Pillow.
"""

import pathlib

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1200, 630
BG = (22, 20, 15)
INK = (234, 230, 223)
MUTED = (154, 148, 138)
ACCENT = (217, 138, 111)
MARGIN = 90

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "og.png"


def main() -> None:
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)

    name_font = ImageFont.truetype(SERIF, 96)
    sub_font = ImageFont.truetype(SANS, 40)
    small_font = ImageFont.truetype(SANS, 30)

    draw.rectangle([MARGIN, 250, MARGIN + 90, 258], fill=ACCENT)
    draw.text((MARGIN, 285), "Josh Hills", font=name_font, fill=INK)
    draw.text((MARGIN, 405), "AI Security Researcher", font=sub_font, fill=MUTED)
    draw.text((MARGIN, 470), "Evaluations \u00b7 AI control \u00b7 red-teaming", font=small_font, fill=MUTED)
    draw.text((MARGIN, HEIGHT - 90), "josh-hills.github.io", font=small_font, fill=ACCENT)

    img.save(OUT)
    print(f"wrote {OUT} {img.size}")


if __name__ == "__main__":
    main()
