from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        w_count = get_word_count(text)
        c_count = get_char_count(text)
        print_report(filepath, w_count, c_count)

def main():
    get_book_text("books/frankenstein.txt")

main()
