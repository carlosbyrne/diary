def grammar_check(text: str):
    if text == "" or not isinstance(text, str):
        raise Exception("Invalid input.")
    valid_puncs = ".!?"
    return text[0].isupper() and text[-1] in valid_puncs
