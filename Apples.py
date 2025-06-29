import random
class Apples:
    count=0
    total_weight=0
    cont=True
    def __init__(self):
        self.weight = random.uniform(0.2, 0.5)
        if (((Apples.total_weight + self.weight)< 300)and ((Apples.count+1) < 1000)):
            Apples.total_weight += self.weight
            Apples.count += 1
        else:
            Apples.cont=False 
            
while(Apples.cont):
    apple=Apples()
else:
    print("Created {} apples, total weight{}".format(Apples.count,Apples.total_weight))
    
            
