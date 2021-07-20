def count_word_entry(word, filename):
    try:
        with open(filename, "r") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"File {filename} doesn't exist.")
    else:
        entry_count = contents.lower().count(word)
        times = "time" if entry_count == 1 else "times"
        print(f"Word '{word}' is met in '{filename}' {entry_count} {times}.")


if __name__ == "__main__":
    count_word_entry(" the ", "62095-0.txt")
    count_word_entry(" the ", "pg13785.txt")