#remove any .,-,space from phone number via a list comprehension
#if len.list is 10 return list[0] as a string
#if len list > 10 delete list[0] und dann return list[0]

class Phone(object):

    def __init__(self, phone_number):
        self.phone_number = phone_number
    
    def number (self):
       self.numbers = [item for item in self.phone_number if item.isnumeric()]
       if len(self.numbers) == 10:
           return ''.join(map(str, self.numbers))
       if len(self.numbers) >10 and self.numbers[0] == "1":
           return ''.join(map(str, self.numbers[1::]))
       raise ValueError ("incorrect phone mumber format")
    
    def __repr__(self):
        return f"{self.number()}"


number = Phone("+1 (223) 456-7890") 
print(number)