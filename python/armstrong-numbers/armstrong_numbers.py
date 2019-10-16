def is_armstrong_number(number):
    result = 0
    numbers = [int(item) for item in str(number)]
    for num in numbers:
        num = num**len(numbers)
        result += num
    if result == number:
        return True
    return False

print(is_armstrong_number(154))  