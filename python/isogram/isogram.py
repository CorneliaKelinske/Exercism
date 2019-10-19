def is_isogram(string):
    string = [char.lower() for char in string if char not in (" ", "-")]
    no_duplicates = set(string)
    if len(no_duplicates) == len(string):
        return True
    return False




