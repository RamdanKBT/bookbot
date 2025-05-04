from stats import get_num_words
from stats import count_characters

def get_book_text(path_to_file):
    with open(path_to_file, "r" , encoding="utf-8") as f:
       text = f.read()
    return text    


def main():
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    words_in_text = get_num_words(book_text)
    letter_count_in_text = count_characters(book_text)
    print(book_text)
    print(words_in_text)
    print(letter_count_in_text)

main()
