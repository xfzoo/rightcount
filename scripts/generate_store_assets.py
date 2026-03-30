#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFilter, ImageFont


PROJECT_DIR = Path(__file__).resolve().parent.parent
ICONS_DIR = PROJECT_DIR / "icons"
STORE_ASSETS_DIR = PROJECT_DIR / "store-assets"

ICON_BG = (18, 20, 24, 255)
ICON_FG = (255, 255, 255, 255)
ACCENT = (93, 162, 255, 255)
SURFACE = (248, 250, 252, 255)
SURFACE_ALT = (240, 244, 249, 255)
TEXT = (24, 33, 44, 255)
MUTED = (108, 121, 137, 255)
SELECTION = (206, 229, 255, 255)
SHADOW = (15, 23, 42, 34)


def load_font(size: int, *, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def rounded_rect(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], radius: int, fill, outline=None, width: int = 1) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def create_icon_base(size: int = 512) -> Image.Image:
    image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    outer_margin = 36
    shadow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    rounded_rect(
        shadow_draw,
        (outer_margin, outer_margin + 14, size - outer_margin, size - outer_margin + 14),
        radius=112,
        fill=(0, 0, 0, 110),
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(28))
    image.alpha_composite(shadow)

    rounded_rect(
        draw,
        (outer_margin, outer_margin, size - outer_margin, size - outer_margin),
        radius=112,
        fill=ICON_BG,
        outline=(255, 255, 255, 28),
        width=5,
    )

    badge_w = 248
    badge_h = 138
    badge_x = (size - badge_w) // 2
    badge_y = (size - badge_h) // 2
    rounded_rect(
        draw,
        (badge_x, badge_y, badge_x + badge_w, badge_y + badge_h),
        radius=54,
        fill=(255, 255, 255, 18),
        outline=(255, 255, 255, 42),
        width=3,
    )

    font = load_font(118, bold=True)
    label = "12"
    left, top, right, bottom = draw.textbbox((0, 0), label, font=font)
    text_w = right - left
    text_h = bottom - top
    draw.text(
        ((size - text_w) / 2, (size - text_h) / 2 - 10),
        label,
        font=font,
        fill=ICON_FG,
    )

    dot_size = 18
    draw.ellipse(
        (
            badge_x + badge_w - 56,
            badge_y + 18,
            badge_x + badge_w - 56 + dot_size,
            badge_y + 18 + dot_size,
        ),
        fill=ACCENT,
    )
    return image


def save_icon_set() -> None:
    ICONS_DIR.mkdir(parents=True, exist_ok=True)
    base = create_icon_base()
    for size in (16, 32, 48, 128):
        icon = base.resize((size, size), Image.Resampling.LANCZOS)
        icon.save(ICONS_DIR / f"icon{size}.png")


def draw_browser_mock(image: Image.Image, *, bubble_text: str, title: str, subtitle: str) -> None:
    draw = ImageDraw.Draw(image)
    width, height = image.size

    for y in range(height):
        blend = y / max(height - 1, 1)
        color = (
            int(SURFACE[0] * (1 - blend) + SURFACE_ALT[0] * blend),
            int(SURFACE[1] * (1 - blend) + SURFACE_ALT[1] * blend),
            int(SURFACE[2] * (1 - blend) + SURFACE_ALT[2] * blend),
            255,
        )
        draw.line([(0, y), (width, y)], fill=color, width=1)

    card_margin_x = 86 if width >= 1000 else 44
    card_margin_y = 60 if height >= 500 else 32
    card = (card_margin_x, card_margin_y, width - card_margin_x, height - card_margin_y)

    shadow = Image.new("RGBA", image.size, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    rounded_rect(
        shadow_draw,
        (card[0], card[1] + 14, card[2], card[3] + 14),
        radius=26,
        fill=SHADOW,
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))
    image.alpha_composite(shadow)
    draw = ImageDraw.Draw(image)

    rounded_rect(draw, card, radius=26, fill=(255, 255, 255, 255), outline=(20, 30, 40, 18), width=2)

    toolbar_h = 70 if height >= 500 else 54
    draw.rounded_rectangle(
        (card[0], card[1], card[2], card[1] + toolbar_h),
        radius=26,
        fill=(245, 247, 250, 255),
    )
    draw.rectangle((card[0], card[1] + toolbar_h - 24, card[2], card[1] + toolbar_h), fill=(245, 247, 250, 255))

    for idx, color in enumerate(((255, 95, 86, 255), (255, 189, 46, 255), (39, 201, 63, 255))):
        x = card[0] + 24 + idx * 18
        y = card[1] + 24
        draw.ellipse((x, y, x + 12, y + 12), fill=color)

    font_title = load_font(34, bold=True)
    font_body = load_font(21)
    font_small = load_font(17)
    font_bubble = load_font(28, bold=True)

    body_left = card[0] + 66
    body_top = card[1] + toolbar_h + 42

    draw.text((body_left, body_top), title, fill=TEXT, font=font_title)
    draw.text((body_left, body_top + 54), subtitle, fill=MUTED, font=font_small)

    paragraph_y = body_top + 120
    line_spacing = 38
    lines = [
        "Right-click selected text and get an instant count bubble.",
        "Chinese characters are counted by character.",
        "English is counted by word, punctuation ignored.",
        "Everything runs locally in Chrome.",
    ]

    selection_line_index = 1
    highlight_x1 = body_left - 10
    highlight_x2 = min(card[2] - 90, body_left + 520)
    highlight_y1 = paragraph_y + selection_line_index * line_spacing - 6
    highlight_y2 = highlight_y1 + 32
    rounded_rect(
        draw,
        (highlight_x1, highlight_y1, highlight_x2, highlight_y2),
        radius=10,
        fill=SELECTION,
    )

    for idx, line in enumerate(lines):
        draw.text((body_left, paragraph_y + idx * line_spacing), line, fill=TEXT, font=font_body)

    bubble_w = 92 if len(bubble_text) <= 2 else 106
    bubble_h = 52
    bubble_x = card[0] + 30
    bubble_y = card[3] - bubble_h - 28
    rounded_rect(
        draw,
        (bubble_x, bubble_y, bubble_x + bubble_w, bubble_y + bubble_h),
        radius=18,
        fill=(19, 22, 28, 235),
        outline=(255, 255, 255, 40),
        width=2,
    )
    left, top, right, bottom = draw.textbbox((0, 0), bubble_text, font=font_bubble)
    text_w = right - left
    text_h = bottom - top
    draw.text(
        (bubble_x + (bubble_w - text_w) / 2, bubble_y + (bubble_h - text_h) / 2 - 4),
        bubble_text,
        fill=ICON_FG,
        font=font_bubble,
    )


def save_store_images() -> None:
    STORE_ASSETS_DIR.mkdir(parents=True, exist_ok=True)

    screenshot1 = Image.new("RGBA", (1280, 800), SURFACE)
    draw_browser_mock(
        screenshot1,
        bubble_text="42",
        title="RightCount",
        subtitle="A lightweight right-click count bubble for web pages",
    )
    screenshot1.save(STORE_ASSETS_DIR / "screenshot-1.png")

    screenshot2 = Image.new("RGBA", (1280, 800), SURFACE)
    draw_browser_mock(
        screenshot2,
        bubble_text="18",
        title="Count mixed Chinese and English correctly",
        subtitle="Chinese by character, English by word, punctuation ignored",
    )
    screenshot2.save(STORE_ASSETS_DIR / "screenshot-2.png")

    promo = Image.new("RGBA", (440, 280), SURFACE)
    draw_browser_mock(
        promo,
        bubble_text="24",
        title="",
        subtitle="",
    )
    promo.save(STORE_ASSETS_DIR / "small-promo-440x280.png")

    marquee = Image.new("RGBA", (1400, 560), SURFACE)
    draw_browser_mock(
        marquee,
        bubble_text="36",
        title="Right-click selected text to count instantly",
        subtitle="Minimal, local, and built for mixed Chinese and English text",
    )
    marquee.save(STORE_ASSETS_DIR / "marquee-1400x560.png")


def main() -> None:
    save_icon_set()
    save_store_images()
    print(f"Generated icons in {ICONS_DIR}")
    print(f"Generated store assets in {STORE_ASSETS_DIR}")


if __name__ == "__main__":
    main()
