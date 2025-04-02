from stats import get_count_characters, get_num_words


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():
    file_content = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(file_content)
    print(f"{num_words} words found in the document")

    print(get_count_characters(file_content))


main()
