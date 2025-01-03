def main():
    book_path = "books/frankenstein.txt"
    book_report(book_path)
    

def book_report(book_path):
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    characters = get_characters_count(book_text)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print(" ")
    
    for character, count in sorted(characters.items()):
        print(f"The '{character}' character was found {count} times")
    print("--- End report ---")


def count_words(text):
    return len(text.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_characters_count(text):
    characters = {"frankenstein": 0, "victor": 0, "elizabeth": 0}
    for word in text.split():
        word = word.lower().strip('.,!?";:')
        if word in characters:
            characters[word] += 1
    return characters
    

if __name__ == '__main__':
    main()