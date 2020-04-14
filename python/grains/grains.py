def square(number):
    if number not in range(1,65):
        raise ValueError("number needs to be between 1 and 64")
    elif number == 1:
        return 1
    return 2**(number-1)


def total():
    total = 0
    number = 1
    while number <= 64:
        total += square(number)
        number+=1
    return total
