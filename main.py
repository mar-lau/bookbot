def get_word_count(text):
    text_array = text.split()
    num_words = len(text_array)
    print(f"{num_words} words found in the document")

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        get_word_count(text)

def main():
    get_book_text("./books/frankenstein.txt")

main()
