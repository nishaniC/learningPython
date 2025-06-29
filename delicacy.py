import copy
class Delicacy:
    def __init__(self,name,price,weight):
        self.name=name
        self.price=price
        self.weight=weight
    
    def __str__(self):
        return "Name: "+self.name+"\n"+"Price: "+ str(self.price) + "\n"+"Weight: " + str(self.weight)
    
delicacy1 = Delicacy("gummy",12,22)
delicacy2=copy.copy(delicacy1)
delicacy3=copy.deepcopy(delicacy1)
delicacy4=copy.deepcopy(delicacy2)
print(delicacy1)
print(delicacy2)
print(delicacy3)
print(delicacy4)

print("Memory chunks:", id(delicacy1), id(delicacy2))
print("Same memory chunk?", delicacy1 is delicacy2)
print("Memory chunks:", id(delicacy3), id(delicacy1))
print("Same memory chunk?", delicacy1 is delicacy3)
