class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.total_minutes = hour * 60 + minute


    def __convert__(self, minutes):
        minute = minutes % 60
        #print(minute)
        if minutes >= 0:
            total_hours = int(minutes/60)
        else:
            if minutes % 60 == 0:
                total_hours = int(minutes/60)
            else:
                total_hours = int(minutes/60)-1
        #print(total_hours)

        if total_hours >= 0:
            #print("going through the hour is greater than or 0 loop")
            if total_hours <= 23:
                #print("going through the hour is smaller than 23 loop")
                hour = total_hours
            
            else:
                #print("going through the hour is greater than 23 loop")
                hour = total_hours % 24
        else:
            #print("going through the hour is negative loop")
            if abs(total_hours) <= 24:
                #print("going through the absolute value of the hour is smaller or equal to 24 loop")
                hour = 24 - abs(total_hours)
            else:
                #print("going through the absolute value of the hour is greater than 24 loop")
                hour = 24 - abs(total_hours) % 24
        if hour == 24:
            hour = 0

        return(f"{str(hour).zfill(2)}:{str(minute).zfill(2)}")

    def __repr__(self):
        return self.__convert__(self.total_minutes)
    
    def __eq__(self, other):
        other_total_minutes = other.hour*60 + other.minute
        if self.__convert__(other_total_minutes) == self.__convert__(self.total_minutes):
            return True
        return False
    
    def __add__(self, minutes):
        new_total_minutes=self.total_minutes+minutes
        return self.__convert__(new_total_minutes)
    
    def __sub__(self, minutes):
        new_total_minutes=self.total_minutes-minutes
        return self.__convert__(new_total_minutes)

test_clock = Clock(2, 20)
print(test_clock.__sub__(3000))