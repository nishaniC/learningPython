import copy
warehouse = list()
warehouse.append({'name': 'Lolly Pop', 'price': 0.4, 'weight': 133})
warehouse.append({'name': 'Licorice', 'price': 0.1, 'weight': 251})
warehouse.append({'name': 'Chocolate', 'price': 1, 'weight': 601})
warehouse.append({'name': 'Sours', 'price': 0.01, 'weight': 513})
warehouse.append({'name': 'Hard candies', 'price': 0.3, 'weight': 433})

print('Source list of candies')
for item in warehouse:
    print(item)
    
warehouse2 = copy.deepcopy(warehouse)
for item in warehouse2:
    if item['weight']>300:
        item['price']-= (item['price']*2)/10
print('Price proposal')
for item in warehouse2:
    print(item)






import copy
class Delicacy:
    def __init__(self,name,price,weight):
        self.name=name
        self.price=price
        self.weight=weight
    
    def __str__(self):
        return "Name: "+self.name+",\t"+"Price: "+ str(self.price) + ",\t"+"Weight: " + str(self.weight)
    

warehouse = list()
warehouse.append(Delicacy('Lolly Pop',  0.4,  133))
warehouse.append(Delicacy('Licorice', 0.1, 251))
warehouse.append(Delicacy('Chocolate', 1,  601))
warehouse.append(Delicacy('Sours',  0.01,  513))
warehouse.append(Delicacy('Hard candies',0.3, 4330))
print('Source list of candies')
for item in warehouse:
    print(item)
    
warehouse2 = copy.deepcopy(warehouse)
for item in warehouse2:
    if item.weight>300:
        item.price-= (item.price*2)/10
print('Price proposal')
for item in warehouse2:
    print(item)
    
print('Source list of candies')
for item in warehouse:
    print(item)
    
warehouse3 = copy.copy(warehouse)
for item in warehouse3:
    if item.weight>300:
        item.price-= (item.price*2)/10
print('Price proposal2')
for item in warehouse3:
    print(item)
    
print('Source list of candies')
for item in warehouse:
    print(item)
    
    # 200,200,100, 100, 50
