import re

def abbreviate(words):
    words = words.replace("'", "")    
    words = re.findall('[(a-z)|(A-Z)]+', words)
    
    result = []
    for item in words:
        result.append(item[0])
    return "".join(result).upper()

