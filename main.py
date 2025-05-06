from stats import get_num_words
from stats import count_characters
from stats import sort_characters_counts
import sys

def get_book_text(path_to_file):   
    with open(path_to_file, "r" , encoding="utf-8") as f:
       text = f.read()
    return text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    words_in_text = get_num_words(book_text)
    letter_count_in_text = count_characters(book_text)
    sorted_character_list = sort_characters_counts(letter_count_in_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {words_in_text} total words")
    print("--------- Character Count -------")
    for item in sorted_character_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()
