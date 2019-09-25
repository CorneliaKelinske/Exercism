def convert(number):
    conversion = {3 : "Pling", 5 : "Plang", 7 : "Plong"}
    code = ''.join([value for key, value in conversion.items() if number % key == 0])
    if code:
        return code
    return str(number)

   
