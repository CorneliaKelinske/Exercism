import inflect
p = inflect.engine()

def nth(num):
    if num == 1:
        return "first" 
    elif num == 2:
        return "second"
    elif num == 3:
        return "third"
    elif num == 5:
        return "fifth"
    elif num == 8:
        return "eigth"
    elif num == 9:
        return "nineth"
    elif num == 12:
        return "twelveth"
    else:
        return f"{p.number_to_words(num)}th"

print(nth(1))
print(nth(9))
print(nth(4))
    
