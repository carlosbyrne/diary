def estimate_reading_time(text):
    if text == "" or not isinstance(text, str):
        raise Exception("Invalid input.")
    one_min_words = 200
    words = len(text.split())
    time = words / one_min_words
    return time

