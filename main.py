from stats import number_words

filename = "/home/david/workspace/github.com/DavidV-NL/Bookbot/books/frankenstein.txt"

def get_book_text(file):
    file_contents = ""
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def number_words():
    text = get_book_text(filename)
    number_of_words = len(text.split())
    return print(f"{number_of_words} words found in the document")

def main():
    return number_words()

main()