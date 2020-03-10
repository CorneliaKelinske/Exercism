def remove_duplicates(numbers):    
    return list(dict.fromkeys(numbers))


def equilateral(sides):
    if len(remove_duplicates(sides)) == 1:
        return True
    return False


def isosceles(sides):
    if len(remove_duplicates(sides))>= 2:
        return True
    return False


def scalene(sides):
    if len(remove_duplicates(sides))== 3:
        return True
    return False


# print(equilateral([1,2,2]))
# print(equilateral([1,2,4]))
# print(equilateral([2,2,2]))

print(isosceles([1,2,2]))
print(isosceles([2,3,4]))
print(isosceles([2,2,2]))

print(scalene([1,2,2]))
print(scalene([1,2,4]))
print(scalene([2,2,2]))