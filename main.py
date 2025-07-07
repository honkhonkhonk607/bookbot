import sys
from stats import count_words, count_char, sort_char_counts

# get_book_text function takes a filepath as input and returns the contents of the file as string

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

# main function uses get_book_text function with the relative path to a .txt file
# to print entire contents of the file to the console

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    try:
        book_text = get_book_text(path)
    except FileExistsError:
        print(f"Error: File not found at path '{path}'")
        sys.exit(1)

    num_words = count_words(book_text)
    char_counts = count_char(book_text)
    sorted_chars = sort_char_counts(char_counts)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")



main()
