import random

class Robot:
    names = []

    def __init__(self):
        self.name = self.pick_name()
           
    def __repr__(self):
        return self.name
    
    def pick_name(self):
        first = self._pick_letter()
        second = self._pick_letter()
        third = self._pick_number()
        fourth = self._pick_number()
        fifth = self._pick_number()
        name = first + second + third + fourth + fifth
        if name in Robot.names:
            name = self.pick_name()
        return name

    
    def _pick_letter(self):
        letters = letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
         "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        random.shuffle(letters)
        return letters[0]
    
    def _pick_number(self):
        num = str(random.randint(0,10))
        return num
    
robbie = Robot()
print(robbie)




