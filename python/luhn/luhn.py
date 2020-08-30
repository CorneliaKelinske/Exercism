class Luhn:
    def __init__(self, card_num):
        self.num = [item for item in card_num if item != " "]
           
    def valid(self):
        if len(self.num) <=1 or not all(item.isnumeric() for item in self.num):
            return False        
        else:
            self.num.reverse()
            all_ints = [int(item) for item in self.num]    
            doubled = [item*2 if not index %2 ==0 else item for index, item in enumerate(all_ints)]
            subtracted = [item-9 if not index %2 ==0 and item>9 else int(item) for index, item in enumerate(doubled)]
            return sum(subtracted) %10 == 0
             

