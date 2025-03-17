


def get_book_contents(file_path):
    # func gets string from file.txt
    with open(file_path, "rt") as file:
        contents = file.read()
    return contents


def main():
    
    file_path_relative = "./books/frankenstein.txt"
    book_contents = get_book_contents(file_path_relative)
    print(book_contents)


main()