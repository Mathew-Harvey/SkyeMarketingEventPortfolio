#!/usr/bin/env python3
"""
Build the 1200x630 social sharing card at assets/img/og-card.jpg.

Drop a portrait at assets/img/skye.jpg and re-run; the script uses it
automatically. Without one it falls back to a 2x2 of real campaign work.

    pip install pillow
    python3 tools/make-og-card.py
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")
FONTS = os.path.join(ROOT, "tools", "fonts")
OUT = os.path.join(IMG, "og-card.jpg")

W, H = 1200, 630
PAD = 64
PANEL_W = 440

GROUND = (236, 238, 240)
INK = (16, 22, 32)
GRAPHITE = (86, 98, 112)
ACCENT = (16, 64, 111)
RULE = (205, 212, 220)

PORTRAIT = os.path.join(IMG, "skye.jpg")
FALLBACK = [
    "ig-05-CTErSmSNqIE.jpg",
    "ig-02-CSnUhFOsXi1.jpg",
    "ig-10-CTk7HRfMaDk.jpg",
    "ig-01-CSaaH_6jmiQ.jpg",
    "ig-04-CS5UW3gg9Kv.jpg",
    "ig-12-CT6uXtOsr6f.jpg",
]


def font(name, size):
    path = os.path.join(FONTS, name)
    if not os.path.exists(path):
        sys.exit(f"missing font: {path}\nSee tools/fonts/README.md")
    return ImageFont.truetype(path, size)


def tracked(draw, xy, text, fnt, fill, tracking=0):
    """Draw text with letter-spacing, which Pillow has no native support for."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + tracking
    return x


def cover(im, box_w, box_h):
    """Scale and centre-crop to exactly fill box_w x box_h."""
    src_ratio = im.width / im.height
    box_ratio = box_w / box_h
    if src_ratio > box_ratio:
        h = box_h
        w = round(h * src_ratio)
    else:
        w = box_w
        h = round(w / src_ratio)
    im = im.resize((w, h), Image.LANCZOS)
    left = (w - box_w) // 2
    top = (h - box_h) // 2
    return im.crop((left, top, left + box_w, top + box_h))


def build_panel():
    """The right-hand image panel: the portrait if present, else a 2x2 of work."""
    if os.path.exists(PORTRAIT):
        return cover(Image.open(PORTRAIT).convert("RGB"), PANEL_W, H), True

    # 2x3 of true squares, so the post artwork is never chopped out of shape.
    # The assembled grid is slightly taller than the card and is trimmed evenly
    # top and bottom, which only ever loses a sliver of the outer tiles.
    gap = 2
    cw = (PANEL_W - gap) // 2
    grid_h = cw * 3 + gap * 2
    grid = Image.new("RGB", (PANEL_W, grid_h), GROUND)
    for i, name in enumerate(FALLBACK):
        path = os.path.join(IMG, name)
        if not os.path.exists(path):
            continue
        tile = cover(Image.open(path).convert("RGB"), cw, cw)
        grid.paste(tile, ((i % 2) * (cw + gap), (i // 2) * (cw + gap)))
    top = max(0, (grid_h - H) // 2)
    return grid.crop((0, top, PANEL_W, top + H)), False


def main():
    card = Image.new("RGB", (W, H), GROUND)
    draw = ImageDraw.Draw(card)

    panel, has_portrait = build_panel()
    card.paste(panel, (W - PANEL_W, 0))

    f_name = font("archivo.ttf", 96)
    f_mono = font("plexmono.ttf", 19)
    f_mono_sm = font("plexmono.ttf", 17)

    y = 150
    tracked(draw, (PAD, y), "BRAND · SOCIAL · EVENTS", f_mono, ACCENT, 2.4)

    y += 54
    draw.text((PAD, y), "Skye", font=f_name, fill=INK)
    y += 96
    draw.text((PAD, y), "Harvey", font=f_name, fill=INK)

    y += 132
    draw.line([(PAD, y), (W - PANEL_W - PAD, y)], fill=RULE, width=1)

    y += 26
    tracked(draw, (PAD, y), "MARKETING & EVENTS — PERTH, WA", f_mono_sm, GRAPHITE, 1.8)

    tracked(draw, (PAD, H - PAD - 18), "skye.andagainapps.com", f_mono_sm, ACCENT, 1.4)

    card.save(OUT, "JPEG", quality=88, optimize=True, progressive=True)
    kb = os.path.getsize(OUT) / 1024
    source = "portrait (assets/img/skye.jpg)" if has_portrait else "fallback 2x2 of campaign work"
    print(f"wrote {OUT}  {W}x{H}  {kb:.0f}KB  — panel: {source}")
    if not has_portrait:
        print("note: add assets/img/skye.jpg and re-run to use the portrait instead.")


if __name__ == "__main__":
    main()
