


def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True



def smallest (min_factor, max_factor):
    all_products = []
    palindromes = []
    results = []

    for num_a in range(min_factor, max_factor+1):
        for num_b in range(num_a, max_factor+1):
            all_products.append( [num_a * num_b, (num_a, num_b)])

    for item in all_products:
        if is_palindrome(item[0]):
            palindromes.append(item)
    
    palindromes_only = [item[0] for item in palindromes]
    
    for item in palindromes:
        if item[0] == min(palindromes_only):
            results.append(item)

    
    return {"value" : results[0][0], "factors" : [item[1] for item in results]}

def largest (min_factor, max_factor):
    all_products = []
    palindromes = []
    results = []

    for num_a in range(min_factor, max_factor+1):
        for num_b in range(num_a, max_factor+1):
            all_products.append( [num_a * num_b, (num_a, num_b)])

    for item in all_products:
        if is_palindrome(item[0]):
            palindromes.append(item)
    
    palindromes_only = [item[0] for item in palindromes]
    
    for item in palindromes:
        if item[0] == max(palindromes_only):
            results.append(item)

    
    return {"value" : results[0][0], "factors" : [item[1] for item in results]}
    

print(smallest(1, 9))
print(largest(1,9))