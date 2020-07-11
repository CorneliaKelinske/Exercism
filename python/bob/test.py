#print(len("\t\t\t\t\t\t\t\t\t\t"))

#print(("1, 2, 3 gO!").isupper())
#print(("How are you?")[-1])



string = ("?!@")
if len([letter for letter in string if letter.isalnum()]) == 0:
    print("YES")