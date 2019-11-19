def classify(number):
    factors = [num for num in range (1, number) if number % num == 0]
    sum_factors = sum(factors)
    if number <= 0:
        raise ValueError ("Not a natural number")
    elif sum_factors == number:
        return "perfect"
    elif sum_factors > number:
        return "abundant"
    return "deficient"




#print(classify(-1))
