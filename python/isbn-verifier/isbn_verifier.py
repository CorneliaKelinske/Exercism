def is_valid(isbn):
    isbn_list = [item for item in isbn if item.isalpha() or item.isdigit()]

    if len(isbn_list) != 10:        
        return False
    for i in range(0, len(isbn_list)-1):
        if isbn_list[i].isalpha():
            return False    
    if isbn_list[9].isdigit() or isbn_list[9] == "X":
       
        print("I am here")
        return "HEllO"
            
    return False

print(is_valid("3-598-21508-9"))
