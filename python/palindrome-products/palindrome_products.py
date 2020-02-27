

# def products(num1, num2):
#     all_products = {}
#     for num_a in range(num1, num2+1):
#         for num_b in range(num_a, num2+1):
#             all_products.update({num_a * num_b: (num_a, num_b)})
#     return all_products

def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True

# def all_palindromes(min_factor, max_factor):
#     results = []
#     for key in products(min_factor, max_factor):
#         if is_palindrome(key):
#             results.append(key)
#     return results

# def largest(min_factor, max_factor):
#     all_products = {}
#     palindromes = {}

#     for num_a in range(min_factor, max_factor+1):
#         for num_b in range(num_a, max_factor+1):
#             all_products.update({num_a * num_b: (num_a, num_b)})

#     for key in all_products:
#         if is_palindrome(key):
#             palindromes.update({key : all_products[key]})
#     return max(palindromes)

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
        if item[0] == max(palindromes_only):
            results.append(item)

    
    return results
    
    # smallest_palin = min(palindromes)
    

print(smallest(1, 9))