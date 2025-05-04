def get_book_text(path_to_file):
    with open(path_to_file, "r" , encoding="utf-8") as f:
       text = f.read()
    return text    


def main():
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    print(book_text)
    

main()
