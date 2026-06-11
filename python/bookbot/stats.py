def get_word_count(text_input: str) -> int:
    words_from_text: list[str] = text_input.split()
    num_words: int = len(words_from_text)

    return num_words

def get_char_count(text_input: str) -> dict[str:int]:
    char_count: dict[str:int] = {}

    for char in text_input.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    return char_count

def sort_on(char: tuple[str,int]) -> int:
    return char[1]

def chars_dict_to_sorted_list(char_dict: dict[str:int]) -> list[tuple[str, int]]:
    char_list = []

    for char in char_dict:
        char_tuple = char, char_dict[char]
        char_list.append(char_tuple)

    sorted_char_list = sorted(char_list, reverse=True, key=sort_on)

    return sorted_char_list