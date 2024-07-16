
from datetime import datetime

NumberOfChildren = input("Please input the number of children that you want to check on: ")

AgeForKindergarden = 6
def elegibilityForKindergarden(ChildsAge,name,AgeForKindergarden):
    
    if ChildsAge < AgeForKindergarden:
        years = AgeForKindergarden - ChildsAge
        print(name," can go to kindergarden in another ", years , " years")
        return 1
    
    if ChildsAge == AgeForKindergarden:
        print(name," can go to kindergarden")
        return 2

    if ChildsAge > AgeForKindergarden:
        years = ChildsAge - AgeForKindergarden
        print("child should have started kindergarden ", years , " years earlier")   
        return 3
    

def theYearCheildshouldHavegonetoK(ChildsAge):
    current_year = datetime.now().year
    years = ChildsAge - AgeForKindergarden
    yearForK = current_year - years
    print("child should have started kindergarden on ", yearForK)  

def processChildre(NumberOfChildren):
    NumberOfChildrenLocal = int(NumberOfChildren)
    while (NumberOfChildrenLocal > 0): 
        ChildsAge1 =int(input("Please input the childs age: "))
        ChildsName =input("Please input the childs name: ")
  
        vaueRturned = elegibilityForKindergarden(ChildsAge1,ChildsName,AgeForKindergarden )

        if  vaueRturned == 3 :
            theYearCheildshouldHavegonetoK(ChildsAge1)
       
        NumberOfChildrenLocal = NumberOfChildrenLocal - 1   

    print("Thank you for using AgeofChild")     



processChildre(NumberOfChildren)


