def largest(min_factor, max_factor):
    products = {}
    for num1 in range(min_factor, max_factor+1):
        for num2 in range(min_factor, max_factor+1):
            if num1*num2 in products:                
                products[num1*num2].append([num1, num2])
            else:
                products.update({num1*num2 : [[num1, num2]]})
   
    palindromes = [key for key in products if str(key) == str(key)[::-1]]

   
    lgst_facs = products[max(palindromes)]
    for item in lgst_facs:
        item.sort()
    factors = []
    for item in lgst_facs:
        if item not in factors:
            factors.append(item)
    
    result = (max(palindromes), factors)
    
       
    return result

print(largest(1000,9999))


def smallest(min_factor, max_factor):
    pass
