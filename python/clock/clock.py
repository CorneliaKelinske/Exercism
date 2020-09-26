class Clock:
    def __init__(self, hour, minute):
        if minute < 60:
            self.minute = str(minute).zfill(2)
        else:
            self.minute = minute%60
            hour = int(minute/60) + hour
        if hour < 23:
            self.hour = hour
        else:
            self.hour = hour%24


    def __repr__(self):
        return(f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}")


    def __eq__(self, other):
        pass

    def __add__(self, minutes):
        pass

    def __sub__(self, minutes):
        pass

test_clock = Clock(1, 60)
print(test_clock)