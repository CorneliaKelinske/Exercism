#remove any .,-,space from phone number via a list comprehension
#if len.list is 10 return list[0] as a string
#if len list > 10 delete list[0] und dann return list[0]

class Phone(object):

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.number = self.clean_number()
        self.area_code = self.get_area_code()
        #self.pretty = self.print_pretty()
    
    def clean_number (self):
       self.digits = [item for item in self.phone_number if item.isnumeric()]
       if len(self.digits) == 10:
           result = "".join(map(str, self.digits))
           if int(result[0]) < 2:
               raise ValueError ("invalid area code")
           if int(result[3]) < 2:
               raise ValueError ("invalid area code")
           return result
       if len(self.digits) >10 and self.digits[0] == "1":           
           result = "".join(map(str, self.digits[1::]))
           if int(result[0]) < 2:
               raise ValueError ("invalid area code")
           if int(result[3]) < 2:
               raise ValueError ("invalid area code")
           return result
       raise ValueError ("incorrect phone mumber format")

    def get_area_code(self):
        return self.clean_number()[:3:]
    
    def pretty(self):
        return "(" + self.clean_number()[:3:] + ") " + self.clean_number()[3:6:] + "-" + self.clean_number()[6::]
       
    
    
    
    
    


my_number = Phone("+1(223) 456-7890") 
print(my_number.area_code)
print(my_number.pretty())