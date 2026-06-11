from stats import word_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

# def main(target_path):
#     return get_book_text(target_path)

def main(target_path):
    book = get_book_text(target_path)
    return word_count(book)

main("books/frankenstein.txt")