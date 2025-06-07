from stats import get_words_count, get_char_distribution, prettify_char_distribution
import sys


def main():
    args = get_arguments()
    file_path = args["path_to_book"]
    text = get_book_text(file_path)
    words_count = get_words_count(text)
    char_distribution = get_char_distribution(text)
    pretty_char_distribution = prettify_char_distribution(char_distribution)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print(f"--------- Character Count -------")
    for char_count in pretty_char_distribution:
        if char_count["char"].isalpha():
            print(f"{char_count["char"]}: {char_count["num"]}")
    print(f"============= END ===============")


def get_arguments():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    return {"path_to_book": path_to_book}


def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()


main()
