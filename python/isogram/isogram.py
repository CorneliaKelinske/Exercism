def is_isogram(string):
    string = [char.lower() for char in string if char.isalpha()]
    return len(set(string)) == len(string)





