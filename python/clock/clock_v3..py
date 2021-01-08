class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.total_minutes = hour * 60 + minute


    def __convert__(self, minutes):
        minute = minutes % 60 

        if minutes >= 0 or minutes % 60 == 0:
            total_hours = int(minutes/60)       
        else:
            total_hours = int(minutes/60)-1
        
        if total_hours >= 0:            
            if total_hours <= 23:                
                hour = total_hours            
            else:               
                hour = total_hours % 24
        else:            
            if abs(total_hours) <= 24:                
                hour = 24 - abs(total_hours)
            else:                
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

