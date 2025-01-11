class Timer:
    def __init__(self,hour=0,minute=0,second=0):
        self.__hours=hour
        self.__minutes=minute
        self.__seconds=second

    def __str__(self):
        
        if (self.__seconds==0 and self.__minutes==0 and self.__hours==0 ):
            return f"00:00:00"
        elif(self.__seconds==0 and self.__minutes==0):
            return f"{self.__hours}:00:00"
        elif(self.__seconds==0 and self.__hours==0 ):
            return f"00:{self.__minutes}:00"
        elif(self.__seconds==0):
            return f"{self.__hours}:{self.__minutes}:00"
        elif (self.__minutes==0 and self.__hours==0 ):
            return f"00:00:{self.__seconds}"
        elif (self.__minutes==0 ):
            return f"{self.__hours}:00:{self.__seconds}"
        elif (self.__hours==0 ):
            return f"00:{self.__minutes}:{self.__seconds}"
        else:
            return f"{self.__hours}:{self.__minutes}:{self.__seconds}"
                

    def next_second(self):
        self.__seconds+=1
        if(self.__seconds==60):
            self.__seconds=00
            self.__minutes+=1
        if(self.__minutes==60):
            self.__minutes=00
            self.__hours+=1
        if(self.__hours==24):
            self.__hours=00
            

    def prev_second(self):
        self.__seconds-=1
        if(self.__seconds==-1):
            self.__seconds=00
            self.__minutes-=1
        if(self.__minutes==-1):
            self.__minutes=00
            self.__hours-=1
        if(self.__hours==-1):
            self.__hours=23
            self.__minutes=59
            self.__seconds=59


timer = Timer(23,59,59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
