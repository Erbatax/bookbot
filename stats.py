def get_words_count(text):
    return len(text.split())


def get_char_distribution(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_by_num(dict):
    return dict["num"]


def prettify_char_distribution(char_distribution):
    result = []  # {"char": "b", "num": 4868}
    for char in char_distribution:
        num = char_distribution[char]
        result.append({"char": char, "num": num})
    result.sort(key=sort_by_num, reverse=True)
    return result
