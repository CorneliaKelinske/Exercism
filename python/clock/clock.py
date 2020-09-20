class Clock:
    def __init__(self, hour, minute):
        if minute < 60:
            self.minute = minute
        else:
            self.minute = minute%60
            hour = int(minute/60) + hour
        if hour < 23:
            self.hour = hour
        else:
            self.hour = hour%24


    def __repr__(self):
        return(f"{self.hour}:{self.minute}")


    def __eq__(self, other):
        pass

    def __add__(self, minutes):
        pass

    def __sub__(self, minutes):
        pass

test_clock = Clock(100,0)
print(test_clock)