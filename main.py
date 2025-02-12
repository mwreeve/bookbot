def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    #print(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    character_report(chars_dict)
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()



def sort_on(dict):
    return dict["count"]


def character_report(input_dict):
    list_of_char_dicts = []
    for char in input_dict:
        list_of_char_dicts.append({"char": char, "count": input_dict[char]})
    list_of_char_dicts.sort(reverse=True, key=sort_on)

    for item in list_of_char_dicts:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['count']} times")


    #print(list_of_char_dicts)
    




    
    








main()