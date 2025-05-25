def number_words():
    text = get_book_text(filename)
    number_of_words = len(text.split())
    return print(f"{number_of_words} words found in the document")