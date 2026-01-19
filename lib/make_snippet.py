def make_snippet(user_string: str):
    if not isinstance(user_string, str):
        raise Exception("Invalid input.")
    
    words = user_string.split()
    
    if len(words) > 5:  
        joined = " ".join(words[:5]) + "..."
        return joined
    elif len(words) <= 5:
        return user_string