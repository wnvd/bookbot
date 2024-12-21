PATH = "books/frankenstein.txt"


def get_book_text():
    with open(PATH) as f:
        return f.read()


def count_words(text):
    words = text.split()
    num_of_words = 0
    for i in range(len(words)):
        num_of_words += 1
    return num_of_words


def count_characters(text):
    dict = {}
    words = text.lower().split()
    # each word
    for i in range(len(words)):
        # each char in word
        for j in range(len(words[i])):
            # increment char dict counter
            if words[i][j] in dict.keys():
                dict[words[i][j]] += 1
            else:
                dict[words[i][j]] = 1
    return dict

# bootdev
# def count_characters(text):
#     dict = {}
#     for c in text:
#         lowered = c.lower()
#         if lowered in dict:
#             dict[lowered] += 1
#         else:
#             dict[lowered] = 1
#     return dict

#
# it is criminal it worked
#
# def sort_on(dict):
#     for key in dict:
#         return dict[key]
#
#
# def generate_report(dict):
#
#     # convert in to list of dicts
#     list_of_word_dict = [] 
#     for char in dict:
#         if char.isalpha():
#             list_of_word_dict.append({char: dict[char]})
#
#
#     for i in range(len(list_of_word_dict)):
#         list_dict = list_of_word_dict[i]
#         for val in list_dict:
#             list_of_word_dict.sort(reverse=True, key=sort_on)
#
#     for list_dict in list_of_word_dict:
#         for key in list_dict:
#             print(f"The '{key}' character was found {list_dict[key]} times")

def sort_on(dict):
    return dict["num"]

def dict_to_dict_list(dict):
    list_of_dict = []
    for char in dict:
        if char.isalpha():
            list_of_dict.append({"char": char, "num" : dict[char]})
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

def generate_report(dict):
    list_of_dicts = dict_to_dict_list(dict)
    for d in list_of_dicts:
        print(f"The '{d["char"]}' character was found {d["num"]} times")


def main():
    book_text = get_book_text()

    num_of_words = count_words(book_text)
    count_dict = count_characters(book_text)

    print(f"--- Begin report of {PATH} ---")
    print(f"{num_of_words} words found in the document")
    print("\n")
    # return on alpha characters
    generate_report(count_dict)
    print("--- End report ---")


if __name__ == "__main__":
    main()
