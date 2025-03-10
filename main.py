from stats import num_words
from stats import character_count
from stats import sorted_dict

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = num_words(text)
    characters = character_count(text)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for char_dict in sorted_dict(characters):
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["count"]}")

#def main():
    #text = get_book_text("books/frankenstein.txt")
    #word_count = num_words(text)
    #char_counts = character_count(text)
    #print(f"{word_count} words found in the document")
    #for char, count in char_counts.items():
        #print(f"'{char}': {count}")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


main()