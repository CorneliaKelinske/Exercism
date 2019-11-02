import inflect
p = inflect.engine()
verses = {
    1 :"a Partridge in a Pear Tree.",
    2 : "two Turtle Doves, ",
    3 : "three French Hens, ",
    4 : "four Calling Birds, ",
    5 : "five Gold Rings, ",
    6 : "six Geese-a-Laying, ",
    7 : "seven Swans-a-Swimming, ",
    8 : "eight Maids-a-Milking, ",
    9 : "nine Ladies Dancing, ",
    10 : "ten Lords-a-Leaping, ",
    11 : "eleven Pipers Piping, ",
    12 : "twelve Drummers Drumming, "
}

def recite(day, verse):

    output = ""
    i = 1
    if day == 1:        
        intro = "On the first day of Christmas my true love gave to me: "
    elif day == 2:
        intro = "On the second day of Christmas my true love gave to me: "
    elif day == 8:
        intro = "On the eighth day of Christmas my true love gave to me: "
    else:
        intro = f"On the {p.number_to_words(day)}th day of Christmas my true love gave to me: "

    while i <= verse:
        output = verses[i] + output
        i += 1


    return intro + output


print(recite(1, 1))
print(recite(2, 2))
print(recite(8, 8))