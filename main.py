import sys
from stats import *


def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, char_count_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_info in char_count_sorted:
        if char_info["char"].isalpha():
            print(f"{char_info['char']}: {char_info['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = char_counter(text)
    char_count_sorted = sorted_char_count(char_count)
    print_report(book_path, num_words, char_count_sorted)
   
if __name__ == "__main__":
    main()