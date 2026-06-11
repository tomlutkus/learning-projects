def get_word_count(text_input):
    words_from_text = text_input.split()
    num_words = len(words_from_text)

    return num_words


def get_char_count(text_input):
    char_count = {}

    for char in text_input.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    return char_count