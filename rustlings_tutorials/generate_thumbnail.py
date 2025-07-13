
import os
import requests
from PIL import Image, ImageDraw, ImageFont

# === Configuration ===
WIDTH, HEIGHT = 1280, 720
BACKGROUND_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
ACCENT_COLOR = (211, 69, 22)

LOGO_PNG_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Rust_programming_language_black_logo.svg/1280px-Rust_programming_language_black_logo.svg.png"
LOGO_FILENAME = "rust_logo.png"

TITLE_FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SUBTITLE_FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
TITLE_FONT_SIZE = 90
SUBTITLE_FONT_SIZE = 60

EXERCISES_ROOT = os.path.join(".", "rustlings", "exercises")
THUMBNAILS_ROOT = os.path.join(".", "assets", "images", "thumbnails")

def download_logo():
    if os.path.exists(LOGO_FILENAME):
        print("✅ Rust logo already exists.")
        return

    print("⬇️ Downloading Rust logo PNG...")
    headers = {
        "User-Agent": "RustlingsThumbnailGenerator/1.0 (https://yourchannel.example.com/)"
    }
    response = requests.get(LOGO_PNG_URL, headers=headers)
    response.raise_for_status()
    with open(LOGO_FILENAME, "wb") as f:
        f.write(response.content)
    print("✅ Rust logo PNG downloaded.")

def get_text_size(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    return width, height

def generate_thumbnail(exercise_name: str, output_path: str):
    download_logo()

    img = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype(TITLE_FONT_PATH, TITLE_FONT_SIZE)
    subtitle_font = ImageFont.truetype(SUBTITLE_FONT_PATH, SUBTITLE_FONT_SIZE)

    # Title
    title_text = "Rustlings Exercises"
    title_w, title_h = get_text_size(draw, title_text, title_font)
    draw.text(((WIDTH - title_w) / 2, HEIGHT * 0.1), title_text, fill=ACCENT_COLOR, font=title_font)

    # Subtitle (exercise filename)
    subtitle_text = exercise_name
    sub_w, sub_h = get_text_size(draw, subtitle_text, subtitle_font)
    subtitle_y = HEIGHT * 0.4
    draw.text(((WIDTH - sub_w) / 2, subtitle_y), subtitle_text, fill=TEXT_COLOR, font=subtitle_font)

    # Rust logo below subtitle
    logo = Image.open(LOGO_FILENAME).convert("RGBA")
    logo.thumbnail((200, 200), Image.LANCZOS)
    logo_x = (WIDTH - logo.width) // 2
    logo_y = int(subtitle_y + sub_h + 40)
    img.paste(logo, (logo_x, logo_y), logo)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)
    print(f"🖼️  Thumbnail saved as: {output_path}")

def collect_exercises(root_path):
    """
    Walks through rustlings/exercises and collects all .rs files grouped by subfolder.
    Returns a dict: {subfolder: [exercise_files]}
    """
    exercises = {}
    for dirpath, dirnames, filenames in os.walk(root_path):
        # We want relative subfolder from exercises root
        rel_dir = os.path.relpath(dirpath, root_path)
        # Ignore root "." directory (only add if it's a subfolder)
        if rel_dir == ".":
            rel_dir = ""

        rust_files = [f for f in filenames if f.endswith(".rs")]
        if rust_files:
            exercises[rel_dir] = rust_files
    return exercises

if __name__ == "__main__":
    all_exercises = collect_exercises(EXERCISES_ROOT)

    for subfolder, files in all_exercises.items():
        for ex_file in files:
            # Thumbnail output path: ./assets/images/thumbnails/<subfolder>/<exercise_name>.png
            # If subfolder is "", save directly in thumbnails root
            subfolder_path = subfolder if subfolder != "" else ""
            output_dir = os.path.join(THUMBNAILS_ROOT, subfolder_path)
            thumbnail_path = os.path.join(output_dir, ex_file.replace(".rs", ".png"))

            generate_thumbnail(ex_file, thumbnail_path)
