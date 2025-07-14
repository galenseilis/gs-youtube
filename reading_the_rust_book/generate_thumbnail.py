import os
import argparse
import re
from PIL import Image, ImageDraw, ImageFont

# Constants
WIDTH, HEIGHT = 1280, 720
BACKGROUND_COLOR = (40, 40, 40)
TEXT_COLOR = (255, 255, 255)
ACCENT_COLOR = (255, 100, 0)

CUSTOM_BOLD = "fonts/Roboto-Bold.ttf"
CUSTOM_REGULAR = "fonts/Roboto-Regular.ttf"
BASE_OUTPUT_PATH = "assets/thumbnails"

def load_font(path: str, fallback: str, size: int) -> ImageFont.FreeTypeFont:
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        print(f"⚠️ Warning: Could not load '{path}', using fallback: '{fallback}'")
        return ImageFont.truetype(fallback, size)

def get_text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]

def get_next_episode_number(path: str) -> int:
    if not os.path.exists(path):
        return 1
    episode_dirs = [
        int(match.group(1))
        for name in os.listdir(path)
        if (match := re.match(r"episode_(\d+)", name)) and os.path.isdir(os.path.join(path, name))
    ]
    return max(episode_dirs, default=0) + 1

def generate_thumbnail(episode_number: int, chapter_title: str, base_output_path: str = BASE_OUTPUT_PATH):
    output_dir = os.path.join(base_output_path, f"episode_{episode_number}")
    os.makedirs(output_dir, exist_ok=True)

    img = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    # Load fonts
    title_font = load_font(CUSTOM_BOLD, "DejaVuSans-Bold.ttf", 100)
    chapter_font = load_font(CUSTOM_REGULAR, "DejaVuSans.ttf", 60)
    episode_font = load_font(CUSTOM_BOLD, "DejaVuSans-Bold.ttf", 40)

    # Multi-line title
    title_lines = ["Reading", "The Rust Book"]
    line_spacing = 20  # space between title lines
    title_to_subtitle_gap = 50

    # Measure each title line
    title_sizes = [get_text_size(draw, line, title_font) for line in title_lines]
    total_title_height = sum(h for _, h in title_sizes) + line_spacing * (len(title_lines) - 1)

    # Subtitle (chapter) size
    chapter_width, chapter_height = get_text_size(draw, chapter_title, chapter_font)

    # Vertical layout calculations
    total_block_height = total_title_height + title_to_subtitle_gap + chapter_height
    top_margin = (HEIGHT - total_block_height) // 3

    # Draw title lines
    current_y = top_margin
    for i, line in enumerate(title_lines):
        line_width, line_height = title_sizes[i]
        draw.text(((WIDTH - line_width) / 2, current_y), line, fill=ACCENT_COLOR, font=title_font)
        current_y += line_height + (line_spacing if i < len(title_lines) - 1 else 0)

    # Draw chapter subtitle
    chapter_y = current_y + title_to_subtitle_gap
    draw.text(((WIDTH - chapter_width) / 2, chapter_y), chapter_title, fill=TEXT_COLOR, font=chapter_font)

    # Draw episode number at bottom-left
    episode_text = f"Episode {episode_number}"
    draw.text((50, HEIGHT - 100), episode_text, fill=TEXT_COLOR, font=episode_font)

    # Save image
    output_file = os.path.join(output_dir, "thumbnail.jpg")
    img.save(output_file)
    print(f"✅ Thumbnail saved to: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Generate YouTube thumbnail for 'Reading The Rust Book' series.")
    parser.add_argument("--episode", type=int, help="Episode number (optional). If not set, auto-incremented.")
    parser.add_argument("--title", required=True, help="Chapter title (required).")
    args = parser.parse_args()

    episode_number = args.episode if args.episode is not None else get_next_episode_number(BASE_OUTPUT_PATH)
    generate_thumbnail(episode_number=episode_number, chapter_title=args.title)

if __name__ == "__main__":
    main()
