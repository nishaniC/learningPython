class TimeInterval:
    def __init__(self, hours,mins,seconds):
        if isinstance(hours, int):
            self.hours=hours    
        else:
            raise TypeError("hours has to be an integer")

        if isinstance(mins, int):
            if ((mins <=60)and (mins >=0)):
                self.mins=mins    
            else:
                raise ValueError("mins has to be greater than or equal to zero and less than or equal to 60")
        else:
                raise TypeError("mins has to be an integer")
                
        if isinstance(seconds, int):
            if ((seconds <=60)and (seconds >=0)):
                self.seconds=seconds    
            else:
                raise ValueError("seconds has to be greater than or equal to zero and less than or equal to 60")
        else:
                raise TypeError("seconds has to be an integer")
                
    def __str__(self):
        return str(self.hours)+":"+str(self.mins)+":"+str(self.seconds)
        
    def adding(self,seconds1,seconds2):
        seconds = seconds1+seconds2
        return self.convert(seconds)
    
    def convertToSeconds(self):
        return self.seconds+(self.mins*60)+(self.hours*3600)
        
    def __add__(self,other):
        seconds1=self.convertToSeconds()
        seconds2=other.convertToSeconds()
        return self.adding(seconds1,seconds2)
    
    def __sub__(self,other):
        seconds1=self.convertToSeconds()
        seconds2=-(other.convertToSeconds())
        return self.adding(seconds1,seconds2)
        
    def __mul__(self,other):
        seconds=self.seconds+(self.mins*60)+(self.hours*3600)
        if isinstance(other, int):
            seconds*=other
        return self.convert(seconds)
            
    def convert(self,seconds):
        hours=seconds//3600
        seconds-=hours*3600
        mins=seconds//60
        seconds-=mins*60
        return TimeInterval(hours,mins,seconds)
        
fti=TimeInterval(21,58,50)
sti=TimeInterval(1,45,22)
print(fti+sti)
print(fti-sti)
print(fti*2)

class TimeInterval2(TimeInterval):
    def __init__(self, hours,mins,seconds):
        super().__init__(hours,mins,seconds)
        
    def __add__(self,other):
        if isinstance(other, int):
            other=super().convert(other)
            return TimeInterval.__add__(self,other)
        else:
            return TimeInterval.__add__(self,other)
            
    def __sub__(self,other):
        if isinstance(other, int):
            other=super().convert(other)
        return TimeInterval.__sub__(self,other)
        
            
tti=TimeInterval2(21,58,50)
print(tti+62)
print(tti-62)

            
