import calendar
class MyCalendar(calendar.Calendar):
    def __init__(self):
       super().__init__()
    def count_weekday_in_year(self,year,weekday):
        # 0 is Monday and 6 is Sunday
        numberofDays=0
        if 0<=weekday<=6:
            for i in range(1,13):
                # month = self.monthdays2calendar(year,i)
                for week in self.monthdays2calendar(year,i):
                    day = week[weekday] 
                    if day[0] != 0:
                        numberofDays+=1
                        
                # print(self.monthdays2calendar(year,i))
        else:
            print("wrong weekday, it has to a number between 0 and6 inclusive")
          
        return numberofDays  
            
    
mc=MyCalendar()
print(mc.count_weekday_in_year(2019,0))
print(mc.count_weekday_in_year(2000,6))
