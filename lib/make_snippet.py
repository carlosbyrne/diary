def make_snippet(user_string: str):
    if not isinstance(user_string, str):
        raise Exception("Invalid input.")
    if len(user_string) > 5:
        return user_string[:5] + "..."
    elif len(user_string) <= 5:
        return user_string