import operator
def get_num_words(book_text):
     words = book_text.split()
     num_words = 0
     for word in words:
        num_words += 1
     return num_words

def count_characters(text):
    char_counts = {}
    for char in text:
        lower_char = char.lower()
        char_counts[lower_char] = char_counts.get(lower_char, 0) + 1
    return char_counts

def sort_characters_counts(char_counts):
    sorted_counts_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            sorted_counts_list.append({"char": char, "num": count})
    sorted_counts_list.sort(key=lambda item: item['num'], reverse=True)
    return sorted_counts_list