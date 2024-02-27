def main():
    file_path = "./books/frankenstein.txt"
    file_contents = get_text(file_path)
    word_count = get_word_count(file_contents)
    print(f"The text contains {word_count} words.")

def get_text(file_path):
    with open(file_path) as file:
        return file.read()

def get_word_count(text):
    return len(text.split())

if __name__ == "__main__":
    main()
