class Clock:
    def __init__(self, hour, minute):        
        total_minutes = hour * 60 + minute    
        self.minute = total_minutes % 60 

        if total_minutes >= 0 or total_minutes % 60 == 0:
            total_hours = int(total_minutes/60)       
        else:
            total_hours = int(total_minutes/60)-1
        
        if total_hours >= 0:            
            if total_hours <= 23:                
                self.hour = total_hours            
            else:               
                self.hour = total_hours % 24
        else:            
            if abs(total_hours) <= 24:                
                self.hour = 24 - abs(total_hours)
            else:                
                self.hour = 24 - abs(total_hours) % 24
        if self.hour == 24:
            self.hour = 0
       

    def __repr__(self):
        return(f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}")
    
    def __eq__(self, other):      
        return self.minute == other.minute and self.hour == other.hour
    
    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)
    
    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)

