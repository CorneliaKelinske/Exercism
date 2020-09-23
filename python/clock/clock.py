class Clock:
    def __init__(self, hour, minute):
        if minute < 60:
            self.minute = str(minute).zfill(2)
        else:
            self.minute = minute%60
            hour = str(int(minute/60) + hour).zfill(2)
        if hour < 23:
            self.hour = str(hour).zfill(2)
        else:
            self.hour = str(hour%24).zfill(2)


    def __repr__(self):
        return(f"{self.hour}:{self.minute}")


    def __eq__(self, other):
        pass

    def __add__(self, minutes):
        pass

    def __sub__(self, minutes):
        pass

test_clock = Clock(1, 60)
print(test_clock)