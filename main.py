def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def count_words(string):
    return len(string.split())


def main():
    file_content = get_book_text("books/frankenstein.txt")
    num_words = count_words(file_content)
    print(f"{num_words} words found in the document")


main()
