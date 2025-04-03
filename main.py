import sys

from stats import get_count_characters, get_num_words, sorted_list


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def generate_report(path):
    file_content = get_book_text(path)
    num_words = get_num_words(file_content)
    char_count = get_count_characters(file_content)
    chars = sorted_list(char_count)

    ret = "============ BOOKBOT ============"
    ret += "\r\n"
    ret += f"Analyzing book found at {path}..."
    ret += "\r\n"
    ret += "----------- Word Count ----------"
    ret += "\r\n"
    ret += f"Found {num_words} total words"
    ret += "\r\n"
    ret += "--------- Character Count -------"
    ret += "\r\n"
    for c in chars:
        if c["name"].isalpha():
            ret += f"{c["name"]}: {c["amount"]}"
            ret += "\r\n"
    ret += "============= END ==============="
    return ret


def usage():
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    if len(sys.argv) != 2:
        usage()
    path = sys.argv[1]
    report = generate_report(path)
    print(report)


main()
