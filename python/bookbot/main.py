from stats import get_word_count, get_char_count, chars_dict_to_sorted_list
import sys

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

def print_report(file_path: str, word_count: int, sorted_chars: list[tuple[str, int]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for line in sorted_chars:
        if line[0].isalpha():
            print(f"{line[0]}: {line[1]}")
    print("============= END ===============")

def main(target_path: str) -> None:
    book = get_book_text(target_path)
    num_words = get_word_count(book)
    chars_dict = get_char_count(book)
    sorted_chars_list = chars_dict_to_sorted_list(chars_dict)
    print_report(target_path, num_words, sorted_chars_list)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(sys.argv[1])