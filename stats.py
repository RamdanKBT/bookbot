def get_num_words(book_text):
     words = book_text.split()
     num_words = 0
     for word in words:
        num_words += 1
     return f"{num_words} words found in the document"

def count_characters(text):
    char_counts = {}
    for char in text:
        lower_char = char.lower()
        char_counts[lower_char] = char_counts.get(lower_char, 0) + 1
    return char_counts