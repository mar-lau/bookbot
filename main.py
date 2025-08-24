from stats import get_word_count

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        get_word_count(text)

def main():
    get_book_text("./books/frankenstein.txt")

main()
