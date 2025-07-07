# count_words function counts the number of words in the string

def count_words(text):
    words = text.split()
    return len(words)

# char_count function counts the number of characters in the string

def count_char(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# sort_char_counts funtion sorts char_count from greatest to least by count 
# it also only includes letters

def sort_char_counts(char_dict):
    sorted_list = []

    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list