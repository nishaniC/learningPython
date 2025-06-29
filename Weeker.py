
class WeekDayError(Exception):
    pass
	

class Weeker:
    #
    # Write code here.
    #

    def __init__(self, day):
        day=day.capitalize()
        self.__week=["Mon","Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        if day in self.__week:
            i=0
            for d in self.__week:
                if day==d:
                    self.__day=day
                    self.__dnumber=i
                else:
                    i+=1
                 
        else:
            raise WeekDayError 
            
    def __str__(self):
        return f"{self.__day}"
    
    def add_days(self, n):
        self.__dnumber+=n
        if self.__dnumber>6:
            self.__dnumber%=7
        self.__day=self.__week[self.__dnumber]
        

    def subtract_days(self, n):
        self.__dnumber-=n
        self.__dnumber%=7
        self.__day=self.__week[self.__dnumber]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
