def square_of_sum(number):
    return (sum([item for item in range(1, number+1)]))**2
  


def sum_of_squares(number):
    return (sum([item**2 for item in range (1, number+1)]))


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)

print(difference_of_squares(10))
