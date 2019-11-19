def classify(number):
    factors = [num for num in range (1, number) if number % num == 0]
    sum_factors = sum(factors)
    if sum_factors == number:
        return "perfect"
    elif sum_factors > number:
        return "abundnat"
    return "deficient"




print(classify(6))
