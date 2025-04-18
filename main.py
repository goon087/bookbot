import sys
from stats import get_num_words, get_chars_dict, sort_on

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(book_path, num_words, chars_dict)
    
    
    
    






def print_report(book_path, num_words, chars_dict):
    print("============ BOOKBOT ==============")
    print(f"Analyzing book found at {book_path}...")
    print("------------ Word Count ------------")
    print(f"Found {num_words} total words")
    print("------------ Character Count ------------")
    chars_list = list(chars_dict.items())
    chars_list.sort(reverse=True, key=sort_on)
    
    for char, count in chars_list:
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============ END ==============")


def get_book_text(path):
    with open(path) as f:
        return f.read()

    



if __name__ == "__main__":
    main()










































