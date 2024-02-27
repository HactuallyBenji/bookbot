def main():
    with open("./books/frankenstein.txt") as file:
        file_contents = file.read()
        print(file_contents)

        words = file_contents.split()
        print(len(words))

if __name__ == "__main__":
    main()
