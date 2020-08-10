class Luhn:
    def __init__(self, card_num):
        self.num = [item for item in card_num if item != " "]
        print(self.num)
        

    def valid(self):
        if len(self.num) <=1:
            return False
        elif:
            
        else:
            self.num.reverse()
           
            doubled = [int(item)*2 if not index %2 ==0 else item for index, item in enumerate(self.num)]
            subtracted = [int(item)-9 if not index %2 ==0 and item>9 else int(item) for index, item in enumerate(doubled)]
            if sum(subtracted) %10 == 0:
                return True
            return False
            


card = Luhn("059a")
print(card.valid())