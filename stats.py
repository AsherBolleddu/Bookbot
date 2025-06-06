def get_num_of_words(content):
    return f"Found {len(content.split())} total words"

def get_num_of_chars(content):
    char_dict = {}
    for char in content.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]  

def sorted_list_char(char_dict):
    sorted_dict_list = []
    for key in char_dict:
        sorted_dict_list.append({"char": key, "num": char_dict[key]})
    sorted_dict_list.sort(reverse=True, key=sort_on)
    return sorted_dict_list