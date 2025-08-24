from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        w_count = get_word_count(text)
        c_count = get_char_count(text)
        print_report(filepath, w_count, c_count)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>");
        sys.exit(1)
    get_book_text(sys.argv[1])

main()
