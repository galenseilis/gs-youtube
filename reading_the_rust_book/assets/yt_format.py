def read_tags_and_print_comma_delimited(filename="tags.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        tags = [line.strip() for line in f if line.strip()]
    print(", ".join(tags))

if __name__ == "__main__":
    read_tags_and_print_comma_delimited()
