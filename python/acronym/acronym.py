import re

def abbreviate(words):
    words = words.replace("'", "")
    letters = re.compile('[(a-z)|(A-Z)]')
    words = re.findall(letters, words) 

    # words = re.sub(not_letter, " ", words)
    print(words)
    # words = words.split(" ")
    # words = [item for item in words if item != ""]

    result = []
    for item in words:
        result.append(item[0])
    return "".join(result).upper()

print(abbreviate("Something - I made up from thin air"))