from stats import get_book_contents, get_word_amount, get_book_stats, sort_stats
import sys

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path_relative = sys.argv[1]
    book_contents = get_book_contents(file_path_relative)
    word_amount = get_word_amount(book_contents)
    book_stats = sort_stats(get_book_stats(book_contents))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path_relative}...")
    print("----------- Word Count ----------")
    print(f"Found {word_amount} total words")
    print("--------- Character Count -------")

    for element in book_stats:
        if element[0].isalpha():
            print(f"{element[0]}: {element[1]}")

    
main()