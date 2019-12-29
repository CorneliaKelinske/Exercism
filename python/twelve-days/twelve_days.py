ordinals = [
    "first", "second", "third", "fourth",
    "fifth", "sixth", "seventh", "eighth",
    "ninth", "tenth", "eleventh", "twelfth"
    ]

gift_list = [
    "a Partridge in a Pear Tree.", "two Turtle Doves, and ", "three French Hens, ",
    "four Calling Birds, ", "five Gold Rings, ", "six Geese-a-Laying, ",
    "seven Swans-a-Swimming, ", "eight Maids-a-Milking, ", "nine Ladies Dancing, ",
    "ten Lords-a-Leaping, ", "eleven Pipers Piping, ", "twelve Drummers Drumming, "
]


def gifts(num):
   gift = gift_list[num - 1]
   
   if num > 1:
        result = gift + str(gifts(num-1))
        
   else:
        result = gift
   return result

def recite(start_verse, end_verse):   
    return [(f"On the {ordinals[verse-1]} day of Christmas my true love gave to me: {gifts(verse)}") for verse in range(start_verse, end_verse+1)]

#print(recite(1,10))
print(recite(1, 1))
print(recite(1, 2))
#print(recite(2, 5))