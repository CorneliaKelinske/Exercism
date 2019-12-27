import inflect
p = inflect.engine()

#def nth(num):
#     if num == 1:
#         return "first" 
#     elif num == 2:
#         return "second"
#     elif num == 3:
#         return "third"
#     elif num == 5:
#         return "fifth"
#     elif num == 8:
#         return "eighth"
#     elif num == 9:
#         return "ninth"
#     elif num == 12:
#         return "twelfth"
#     else:
#         return f"{p.number_to_words(num)}th"
nth = p.ordinal(p.number_to_words(2))
print(nth)
#     return [(f"On the {nth} day of Christmas my true love gave to me: {gifts(verse)}")
#              for verse in range(start_verse, end_verse+1)]

# def gifts(num):
#     if num == 1:
#         gift = "a Partridge in a Pear Tree."
#     elif num == 2:
#         gift = "two Turtle Doves, and "
#     elif num == 3:
#         gift = "three French Hens, "
#     elif num == 4:
#         gift = "four Calling Birds, "
#     elif num == 5:
#         gift = "five Gold Rings, "
#     elif num == 6:
#         gift = "six Geese-a-Laying, "
#     elif num == 7:
#         gift = "seven Swans-a-Swimming, "
#     elif num == 8:
#         gift = "eight Maids-a-Milking, "
#     elif num == 9:
#         gift = "nine Ladies Dancing, "
#     elif num == 10:
#         gift = "ten Lords-a-Leaping, "
#     elif num == 11:
#         gift = "eleven Pipers Piping, "
#     else:
#         gift = "twelve Drummers Drumming, "
    
#     if num > 1:
#         result = gift + str(gifts(num-1))
        
#     else:
#         result = gift
#     return result

# def recite(start_verse, end_verse):
#     return [(f"On the {nth(verse)} day of Christmas my true love gave to me: {gifts(verse)}") for verse in range(start_verse, end_verse+1)]

# print(recite(2, 5))

