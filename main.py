def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_num_words(text)
    alphabet = character_count(text)
    char_list = [{"char":k, "num":v} for k, v in alphabet.items()]
    char_list.sort(reverse=True, key=sort_on)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for i in char_list:
        if i["char"].isalpha():
            print(f"The {i['char']} character was found {i['num']} number of times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["num"]

def count_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    lowered_text = text.lower()
    count_character = {}
    for c in lowered_text:
        if c in count_character:
            count_character[c] += 1
        else:
            count_character[c] = 1
    return count_character

main()