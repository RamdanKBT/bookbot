def get_num_words(book_text):
     words = book_text.split()
     num_words = 0
     for word in words:
        num_words += 1
     return f"{num_words} words found in the document"