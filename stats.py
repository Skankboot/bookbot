def get_book_text (filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def number_of_words (book_path):
    return len(get_book_text (book_path).split())

def number_of_letters (book_path):
    book = get_book_text(book_path)
    letter_count = {}
    for letter in book:
        if letter.lower() in letter_count:
            letter_count[letter.lower()] += 1
        else:
            letter_count[letter.lower()] = 1
    return letter_count

def sort_on(dict):
    return dict["num"]

def sorter (dictionary):
    sorted = []
    for i in dictionary:
        if i.isalpha():
            sorted.append({"char" : i, "num" : dictionary[i]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted