def is_valid(isbn):
    isbn_list = [item for item in isbn if item.isalpha() or item.isdigit()]
    sum = 0
    multiplier = 10

    if len(isbn_list) != 10:        
        return False
    if isbn_list[9] == "X" :
        isbn_list[9] = "10"
    for i in range(0, len(isbn_list)):
        if isbn_list[i].isalpha():
            return False 
    if isbn_list[9].isdigit() or isbn_list[9] == "10":
        for item in isbn_list:
            result = int(item) * multiplier
            sum += result
            multiplier -=1
        if sum % 11 == 0:
            return True
    
      
    return False
       
   

print(is_valid("359821507X"))