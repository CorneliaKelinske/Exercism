#remove any .,-,space from phone number via a list comprehension
#if len.list is 10 return list[0] as a string
#if len list > 10 delete list[0] und dann return list[0]

class Phone(object):

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.number = self.clean_number()
    
    def clean_number (self):
       self.digits = [item for item in self.phone_number if item.isnumeric()]
       if len(self.digits) == 10:
           return "".join(map(str, self.digits))
       if len(self.digits) >10 and self.digits[0] == "1":
           return "".join(map(str, self.digits[1::]))
       raise ValueError ("incorrect phone mumber format")
    
    
    


my_number = Phone("+1(223) 456-7890") 
print(my_number.number)