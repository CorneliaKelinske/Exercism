def largest(min_factor, max_factor):
    products = {}
    for num1 in range(min_factor, max_factor+1):
        for num2 in range(min_factor, max_factor+1):
            if num1*num2 in products:                
                products[num1*num2].append([num1, num2])
            else:
                products.update({num1*num2 : [[num1, num2]]})
    palindromes = [key for key in products if str(key) == str(key)[-1]]
    for item in products[max(palindromes)]:
        item.sort()
    
    return products[max(palindromes)]

print(largest(1,9))   


def smallest(min_factor, max_factor):
    pass
