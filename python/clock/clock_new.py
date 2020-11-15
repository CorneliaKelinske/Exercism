class Clock:
    def __init__(self, hour, minute):
        self.total_minutes = hour * 60 + minute
        #print(self.total_minutes)
        self.minute = self.total_minutes%60
        #print(self.minute)
        if self.total_minutes >= 0:
            total_hours = int(self.total_minutes/60)
        else:
            if self.total_minutes%60 == 0:                
                total_hours=int(self.total_minutes/60)
            else:
                total_hours = int(self.total_minutes/60)-1
        print(total_hours)

        if total_hours >= 0:
            #print("going through the hour is greater than or 0 loop")
            if total_hours <= 23:
                #print("going through the hour is smaller than 23 loop")
                self.hour = total_hours
            else:
                #print("going through the hour is greater than 23 loop")
                self.hour = total_hours%24
        else:
            #print("going through the hour is negative loop")
            if abs(total_hours) <= 24:
                #print("going through the absolute value of the hour is smaller or equal to 24 loop")
                self.hour = 24 - abs(total_hours)
            else:
                #print("going through the absolute value of the hour is greater than 24 loop")
                self.hour = 24 - abs(total_hours)%24
        



    def __repr__(self):
        return(f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}")

    def __add__(self, minutes):
        self.minute += minutes
        
        return(f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}")

test_clock = Clock(-25, 0)
print(test_clock.__add__(40))