from stats import get_num_of_words, get_num_of_chars, sorted_list_char
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_of_chars = get_num_of_chars(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(get_num_of_words(book_text))
    print("--------- Character Count -------")
    char_list = sorted_list_char(num_of_chars)
    for item in char_list:
        if item["char"].isalpha():
            print(item["char"] + ": " + str(item["num"]))
    print("============= END ===============")

main()