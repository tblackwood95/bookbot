def num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    characters = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters

def sorted_dict(characters):
    sorted_list = []
    for letter, count in characters.items():
        sorted_list.append({"char": letter, "count": count})
    sorted_list.sort(key=lambda x: (-x["count"], x["char"]))
    return sorted_list
