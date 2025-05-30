def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    letters = {}
    for char in text:
        if char.lower() not in letters:
            letters[char.lower()] = 0
        letters[char.lower()] += 1
    return letters

def sorted_letter_count(dictionary):
    sorted = []
    for k in dictionary:
        sorted.append({"char":k, "num": dictionary[k]})
    sorted.sort(reverse=True,key=lambda d : d["num"])
    return sorted