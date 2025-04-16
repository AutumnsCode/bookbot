import sys
from stats import get_number_of_words
from stats import get_num_of_character
from stats import sort_chars_by_count

def get_book_text(path):
    with open(path) as file:
        return file.read()

def main(): 
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file = sys.argv[1]
    book_text = get_book_text(file)
    num_words = get_number_of_words(book_text)
    num_chars = get_num_of_character(book_text)
    sorted_counts = sort_chars_by_count(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_counts: 
        char = item['char']
        count = item['count']
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")
    # print(f"{num_words} words found in the document")
    # print(num_chars)

main()
