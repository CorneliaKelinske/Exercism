

import re

def abbreviate(words):
    words = words.replace("'", "")
    not_letter = re.compile(r'[^(a-z)|(A-Z)]')
    words = re.sub(not_letter, " ", words)
    words = words.split(" ")
    words = [item for item in words if item != ""]

    result = []
    for item in words:
        result.append(item[0])
    return "".join(result).upper()


