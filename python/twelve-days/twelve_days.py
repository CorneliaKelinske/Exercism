import inflect
p = inflect.engine()
verses = {
    1 : "a Partridge in a Pear Tree.",
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

def recite(start_verse, end_verse):

    output = ""
    i = 2
    if start_verse == 1:        
        intro = "On the first day of Christmas my true love gave to me: "
    elif start_verse == 2:
        intro = "On the second day of Christmas my true love gave to me: "
    elif start_verse == 3:
        intro = "On the third day of Christmas my true love gave to me: "
    elif start_verse == 5:
        intro = "On the fifth day of Christmas my true love gave to me: "
    elif start_verse == 8:
        intro = "On the eighth day of Christmas my true love gave to me: "
    elif start_verse == 9:       
        intro = "On the ninth day of Christmas my true love gave to me: "
    elif start_verse == 12:       
        intro = "On the twelfth day of Christmas my true love gave to me: "
    else:
        intro = f"On the {p.number_to_words(start_verse)}th day of Christmas my true love gave to me: "

    if start_verse == 1 and end_verse == 1:
        return [intro + verses[1]]
   
    while start_verse < end_verse+1:
        while i <= end_verse:
            output = verses[i] + output
            i += 1
            
    return output


print(recite(1, 1))
print(recite(3, 3))
#print(recite(12, 12))