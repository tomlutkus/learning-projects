from stats import get_word_count, get_char_count, chars_dict_to_sorted_list

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

def main(target_path: str):
    book: str = get_book_text(target_path)
    num_words: int = get_word_count(book)
    chars_dict: dict[str:int] = get_char_count(book)
    sorted_chars_list: list[tuple[str, int]] = chars_dict_to_sorted_list(chars_dict)

    print(f"Found {num_words} total words")

    for line in sorted_chars_list:
        print(line)

main("books/frankenstein.txt")
