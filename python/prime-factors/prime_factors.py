
#def is_prime(number):
#    primes = []
#    for num in range (2, number+1):


#def factors(value):


def factors(value):
    prime_factors = []
    num = 2
    while num <= value:
        print(num)
        if value % num == 0:
            while value % num ==0:
                prime_factors.append(num)
                print(prime_factors)
                value = value/num
                print(value)
            num+=1
            print(num)
        num+=1
    return prime_factors
    
print(factors(60))
