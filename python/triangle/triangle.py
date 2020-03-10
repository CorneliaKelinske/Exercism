def equal_sides(numbers):
    equals = []
    for num1 in numbers:
        for num2 in numbers:
            if num1 == num2:
                equals.append(num1)
    return list(dict.fromkeys(equals))


def equilateral(sides):
    pass


def isosceles(sides):
    pass


def scalene(sides):
    pass


print(equal_sides([1,2,2]))
print(equal_sides([1,2,4]))
print(equal_sides([2,2,2]))