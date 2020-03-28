def abbreviate(words):
    words = words.replace("-", " ")
    print(words)
    words = words.split(" ")
    print(words)

    # for item in words:
    #     if item.isalpha() == False:
    #         words.remove(item)
    result = []
    for item in words:
        result.append(item[0])
    
    # return words

    return "".join(result).upper()


print(abbreviate("The Road _Not_ Taken"))