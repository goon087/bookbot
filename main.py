def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(book_path, num_words, chars_dict)
    
    
    
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict_item):
    return dict_item[1]

def print_report(book_path, num_words, chars_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    
    chars_list = list(chars_dict.items())
    chars_list.sort(reverse=True, key=sort_on)
    
    for char, count in chars_list:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

    



if __name__ == "__main__":
    main()










































