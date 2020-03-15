def remove_duplicates(numbers):    
    return list(dict.fromkeys(numbers))

def triangle_check(numbers):
    for num in numbers:
        if num == 0:
            return False
   
    if not numbers[0] + numbers[1] >= numbers[2]:
        return False
    elif not numbers[0] + numbers[2] >= numbers[1]:
        return False
    elif not numbers[2] + numbers[1] >= numbers[0]:
        return False
    return True



def equilateral(sides):
    if triangle_check(sides) == True:
        if len(remove_duplicates(sides)) == 1:
            return True
    return False


def isosceles(sides):
    if triangle_check(sides) == True:

        if len(remove_duplicates(sides))<= 2:
            return True
    return False


def scalene(sides):
    if triangle_check(sides) == True:
        if len(remove_duplicates(sides))== 3:
            return True
    return False

