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
    if len(remove_duplicates(sides)) == 1:
        return True
    return False


def isosceles(sides):
    if triangle_check(sides) == True:

        if len(remove_duplicates(sides))<= 2:
            return True
    return False


def scalene(sides):
    if len(remove_duplicates(sides))== 3:
        return True
    return False


# print(equilateral([1,2,2]))
# print(equilateral([1,2,4]))
# print(equilateral([2,2,2]))

# print(isosceles([1,2,2]))
# print(remove_duplicates([2,3,4]))
# print(isosceles([2,3,4]))
# print(remove_duplicates([2,2,2]))
# print(isosceles([2,2,2]))

# print(scalene([1,2,2]))
# print(scalene([1,2,4]))
# print(scalene([2,2,2]))

print(triangle_check([1,1,3]))