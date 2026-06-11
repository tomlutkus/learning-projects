def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

def main(book_path):
    book = get_book_text(book_path)
    print(book)

main("books/frankenstein.txt")