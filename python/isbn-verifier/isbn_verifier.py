def is_valid(isbn):
    isbn_list = [item for item in isbn if item.isalpha() or item.isdigit()]

    if len(isbn_list) != 10:
        print("I'm in condition 1")
        return False
    for item in range(isbn_list[0], isbn_list[9]):
        if item.isalpha():
            print("I'm in condition 2")
            return False
    if isbn_list[9] in range(0, 10) or isbn_list[9] == "X":
        return "Hello"
    return isbn_list

print(is_valid("3-598-91581-X"))
