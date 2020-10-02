class Clock:
    def __init__(self, hour, minute):
        if minute >= 0:
            if minute < 60:
                self.minute = minute
            else:
                self.minute = minute%60
                hour = int(minute/60) + hour
        else:
            hour -= hour
            if abs(minute)< 60:
                self.minute = 60 - abs(minute)
            elif abs(minute) == 60:                
                self.minute = 0
            else:
                self.minute = 60 - abs(minute)%60
                hour = hour - int(abs(minute)/60)

        if hour >= 0:
            if hour < 23:
                self.hour = hour
            else:
                self.hour = hour%24
        else:
            if abs(hour) <= 24:
                self.hour = 24 - abs(hour)
            else:
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