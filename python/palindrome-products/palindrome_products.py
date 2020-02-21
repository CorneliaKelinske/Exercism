# def largest(min_factor, max_factor):
#     pass


# def smallest(min_factor, max_factor):
#     pass


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
    all_products = {}
    palindromes = {}

    for num_a in range(min_factor, max_factor+1):
        for num_b in range(num_a, max_factor+1):
            all_products.update({num_a * num_b: (num_a, num_b)})

    for key in all_products:
        if is_palindrome(key):
            palindromes.update({key : all_products[key]})
    
    smallest_palin = min(palindromes)
    return smallest_palin

print(smallest(9, 20))