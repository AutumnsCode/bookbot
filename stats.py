def get_number_of_words(text):
    total_words = text.split()
    return len(total_words)

def get_num_of_character(text): 
    char_count = {}

    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_chars_by_count(char_counts):
    sorted_list = [{'char': char, 'count': count} for char, count in char_counts.items() if char]

    sorted_list.sort(key=lambda item: item['count'], reverse=True)
    return sorted_list