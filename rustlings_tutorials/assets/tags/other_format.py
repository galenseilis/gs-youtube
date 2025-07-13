def read_tags_and_print(filename="tags.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        tags = [f"#{line.strip().replace(' ', '')}" for line in f if line.strip()]
        for tag in tags:
            print(tag)

if __name__ == "__main__":
    read_tags_and_print()
