def main():
    file_path = "./books/frankenstein.txt"
    file_contents = get_text(file_path)
    word_count = get_word_count(file_contents)
    print(f"The text contains {word_count} words.")

    character_counts = get_character_counts(file_contents)
    print(f"The text has many characters. Here's are the frequencies of each.")
    show_character_counts(character_counts)

def get_text(file_path):
    with open(file_path) as file:
        return file.read()

def get_word_count(text):
    return len(text.split())

def get_character_counts(text):
    character_counts = {}
    for character in text:
        character = character.lower()
        if character.isalpha() == False:
            continue
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
    return character_counts

def show_character_counts(character_counts):
    for character, count in character_counts.items():
        print(f"{character}: {count}")

if __name__ == "__main__":
    main()
