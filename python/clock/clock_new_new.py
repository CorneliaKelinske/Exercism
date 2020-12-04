class Clock:
    def __init__(self, hour, minute):
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
                self.hour = total_hours % 24
        else:
            #print("going through the hour is negative loop")
            if abs(total_hours) <= 24:
                #print("going through the absolute value of the hour is smaller or equal to 24 loop")
                hour = 24 - abs(total_hours)
            else:
                #print("going through the absolute value of the hour is greater than 24 loop")
                hour = 24 - abs(total_hours) % 24

        return(f"{str(hour).zfill(2)}:{str(minute).zfill(2)}")

    def __repr__(self):
        return self.__convert__(self.total_minutes)

test_clock = Clock(0, 45)
print(test_clock)