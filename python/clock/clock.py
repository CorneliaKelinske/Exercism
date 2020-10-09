class Clock:
    def __init__(self, hour, minute):
        if minute >= 0:
            #print("going through the minute is greater than or zero loop")
            if minute < 60:
                #print("going through the minute smaller than 60 loop")
                self.minute = minute
            else:
                #print("going through the minute is greater or equal to 60 loop")
                self.minute = minute%60
                hour = int(minute/60) + hour
        else:
            #print("going through the minute is negative loop")
            hour -= 1
            #print("I have deducted one hour")
            #print(hour)
            if abs(minute)< 60:
                #print("going through the absolute value is smaller than 60 loop")
                self.minute = 60 - abs(minute)
            elif abs(minute) == 60:
                #print("going through the absolute value is 60 loop")                
                self.minute = 0
                #print(hour)
            else:
                #print("going through the absolute value is greater than 60 loop")
                self.minute = 60 - abs(minute)%60
                hour = hour - int(abs(minute)/60)

        #print(hour)
        if hour >= 0:
            #print("going through the hour is greater than or 0 loop")
            if hour <= 23:
                #print("going through the hour is smaller than 23 loop")
                self.hour = hour
            else:
                print("going through the hour is greater than 23 loop")
                self.hour = hour%24
        else:
            #print("going through the hour is negative loop")
            if abs(hour) <= 24:
                #print("going through the absolute value of the hour is smaller or equal to 24 loop")
                self.hour = 24 - abs(hour)
            else:
                #print("going through the absolute value of the hour is greater than 24 loop")
                self.hour = 24 - abs(hour)%24
        



    def __repr__(self):
        return(f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}")


    def __eq__(self, other):
        pass

    def __add__(self, minutes):
        pass

    def __sub__(self, minutes):
        pass

test_clock = Clock(2, -60)
print(test_clock)