


def get_book_contents(file_path):
    with open(file_path, "rt") as file:
        contents = file.read()
    return contents

def get_word_amount(str):
    words_arr = str.split()
    return len(words_arr)

def main():
    
    file_path_relative = "./books/frankenstein.txt"
    book_contents = get_book_contents(file_path_relative)
    word_amount = get_word_amount(book_contents)
    print(f"{word_amount} words found in the document")


main()