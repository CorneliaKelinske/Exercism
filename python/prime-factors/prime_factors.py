
def factors(value):
    prime_factors = []
    num = 2
    while num <= value:        
        if value % num == 0:            
            while value % num ==0:               
                prime_factors.append(num)                
                value = value/num                
            num+=1            
        else:
            num+=1
    return prime_factors
    

