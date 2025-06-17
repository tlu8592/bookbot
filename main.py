from stats import get_num_words
from stats import character_count
from stats import sort_dictionary
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents



def print_report(file_path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    num_of_char = character_count(get_book_text(sys.argv[1]))
    num_of_words = get_num_words(get_book_text(sys.argv[1]))
    sorted_list = sort_dictionary(num_of_char)
    print_report(sys.argv[1], num_of_words, sorted_list)

main()