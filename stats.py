def get_num_words(text):
    text_list = text.split()
    count = 0
    for text in text_list:
        count += 1
    return f"Found {count} total words"

def character_count(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_dictionary(num_of_char):
    dict_list = [{'char': char, 'num': num} for char, num in num_of_char.items()]
    dict_list.sort(reverse=True, key=lambda d: d["num"])
    return dict_list
