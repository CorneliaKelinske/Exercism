verses = {
    0 : "a Partridge in a Pear Tree.",
    1 : "and a Partridge in a Pear Tree.",
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

intros = {
    1 : "On the first day of Christmas my true love gave to me: ",
    2 : "On the second day of Christmas my true love gave to me: ",
    3 : "On the third day of Christmas my true love gave to me: ",
    4 : "On the fourth day of Christmas my true love gave to me: ",
    5 : "On the fifth day of Christmas my true love gave to me: ",
    6 : "On the sixth day of Christmas my true love gave to me: ",
    7 : "On the seventh day of Christmas my true love gave to me: ",
    8 : "On the eighth day of Christmas my true love gave to me: ",
    9 : "On the ninth day of Christmas my true love gave to me: ",
    10 : "On the tenth day of Christmas my true love gave to me: ",
    11 : "On the eleventh day of Christmas my true love gave to me: ",
    12 : "On the twelfth day of Christmas my true love gave to me: "
}

def recite(start_verse, end_verse):

    result = ""
    #def get_intro(verse):
        #return intros[verse]
    
    if start_verse == 1 and end_verse == 1:
        return [intros[start_verse] + verses[0]]
    
    for verse in range(start_verse, end_verse+1):
        result += intros[verse]
    return [result]
    # for verse in range (start_verse, end_verse):
    #     result = ""
    #     get_intro(verse)]=      
        
            

       


   

#print(recite(1,1))
#print(recite(5, 5))
print(recite(1,2))