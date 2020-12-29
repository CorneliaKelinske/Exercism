numbers = range(1,4)
products = {}

for num1 in numbers:
    for num2 in numbers:
        products.update({num1*num2 : [(num1, num2)]})


products = {1: [(1, 1)], 2: [(2, 1)], 3: [(3, 1)], 4: [(2, 2)], 6: [(3, 2)], 9: [(3, 3)]}
products[1][len(products[1])-1] = "blue"

#print(products)