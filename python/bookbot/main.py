from stats import get_word_count, get_char_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

# def main(target_path):
#     return get_book_text(target_path)

def main(target_path):
    book = get_book_text(target_path)
    num_words = get_word_count(book)
    chars_list = get_char_count(book)

    print(f"Found {num_words} total words")

    for char in chars_list:
        print(f"'{char}': {chars_list[char]}")

main("books/frankenstein.txt")

