class Luhn:
    def __init__(self, card_num):
        self.num = [item for item in card_num if item.isnumeric()]
        

    def valid(self):
        if len(self.num) <=1:
            return False
        else:
            self.num.reverse()
            #doubled = [int(item)*2 for item in self.num if self.num.index(item) %2 !=0]
            doubled = [int(item)*2 if not index %2 ==0 else item for index, item in enumerate(self.num)]
            return doubled
            


card = Luhn("0545")
print(card.valid())