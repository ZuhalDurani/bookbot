def get_num_words(text):
    words = text.split()
    return len(words)

def char_counter(text):
    ltext = text.lower()
    char_count = {}
    for char in ltext:
      char_count[char] = char_count.get(char,0) + 1  
    return char_count

def return_char_num(char_count_dict):
    return char_count_dict["num"]

def sorted_char_count(char_count_dict):
    sorted_chars = []
    for letter, count in char_count_dict.items():
        sorted_chars.append({"char":letter,"num":count})
    sorted_chars.sort(reverse=True, key=return_char_num)
    return sorted_chars