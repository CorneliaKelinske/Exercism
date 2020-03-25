def abbreviate(words):
    words = words.replace("-", " ")
    words = words.split(" ")
    result = []
    for item in words:
        result.append(item[0])

    return "".join(result)


print(abbreviate("Portable-Network Graphics"))