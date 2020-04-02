# def abbreviate(words):
#     words = words.replace("-", " ")
#     print(words)
#     words = words.split(" ")
#     words = [item for item in words if item != ""]
#     print(words)

#     # for item in words:
#     #     if item.isalpha() == False:
#     #         words.remove(item)
#     result = []
#     for item in words:
#         if item[0].isalpha():
#             result.append(item[0])
#         else:
#             result.append(item[1])
    
#     # return words

#     return "".join(result).upper()

import re
def abbreviate(words):
    not_letter = re.compile(r'[^(a-z)|(A-Z)]')
    words = re.sub(not_letter," ", words)
    return words



print(abbreviate("Something - _I made up from thin air"))
