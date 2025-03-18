


def get_book_contents(file_path):

    with open(file_path, "rt") as file:
        contents = file.read()
    return contents


def get_word_amount(str):

    words_arr = str.split()
    return len(words_arr)


def get_book_stats(str):

    characters_dict = {}
    for char in str:
        char = char.lower()
        if char in characters_dict:
            characters_dict[char] += 1
        else:
            characters_dict.update({char: 1})
    return characters_dict


def sort_stats(book_stats):
    
    sorted_dict = sorted([(key, value) for (key, value) in book_stats.items()])
    return sorted_dict