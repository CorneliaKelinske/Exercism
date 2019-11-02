import inflect
p = inflect.engine()
v1 = "a Partridge in a Pear Tree."
v2 = "two Turtle Doves,"
v3 = "three French Hens,"
v4 = "four Calling Birds,"
v5 = "five Gold Rings,"
v6 = "six Geese-a-Laying,"
v7 = "seven Swans-a-Swimming,"
v8 = "eight Maids-a-Milking,"
v9 = "nine Ladies Dancing,"
v10 = "ten Lords-a-Leaping,"
v11 = "eleven Pipers Piping,"
v12 = "twelve Drummers Drumming,"

def recite(start_verse):
    if start_verse == 1:
        intro = "On the first day of Christmas my true love gave to me: "
    elif start_verse == 2:
        intro = "On the second day of Christmas my true love gave to me: "
    else:
        intro = f"On the {p.number_to_words(start_verse)}th day of Christmas my true love gave to me: "
    
 
    return intro


print(recite(1))
print(recite(2))
print(recite(8))