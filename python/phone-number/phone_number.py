#remove any .,-,space from phone number via a list comprehension
#if len.list is 9 return list[0] as a string
#if len list > 9 delete list[0] und dann return list[0]

class Phone(object):

    def __init__(self, phone_number):
        self.phone_number = phone_number
    
    def format_number(self):
       self.numbers = [item for item in self.phone_number if item not in ("+", "-", ".", "(", ")"," ")]
       return self.numbers
    
    def __repr__(self):
        return f"{self.format_number()}"


number = Phone("(223) 456-7890") 
print(number)