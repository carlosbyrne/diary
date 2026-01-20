
def count_words(user_string: str):
    if not isinstance(user_string, str):
        raise Exception("Invalid input.")
    
    words = user_string.split()
    return len(words)


letter = 'a'
letters = letter * 4

print(letters)