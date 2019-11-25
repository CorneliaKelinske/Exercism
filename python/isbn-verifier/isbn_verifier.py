def is_valid(isbn):
    isbn_list = [item for item in isbn if item.isalpha() or item.isdigit()]

    if len(isbn_list) != 10:        
        return False
    if isbn_list[9] == "X" :
        isbn_list[9] = "10"
    for i in range(0, len(isbn_list)):
        if isbn_list[i].isalpha():
            return False 
    if isbn_list[9].isdigit() or isbn_list[9] == "10":
        return True
    
      
    return type(isbn_list[2])
       
    #     print ((isbn_list[0]*10))
    #     return True
            
    #return False

print(is_valid("3-298-21508-X"))
