def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_num_words(text)
    print(word_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_num_words(text):
    words = text.split()
    return len(words)


main()