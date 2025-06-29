def bmi(weight, height):
    if ((isinstance(weight,int)or isinstance(weight,float))and (isinstance(height,int) or isinstance(height,float))):
        if((weight>0) and (height>0)):
            return weight / height ** 2


print(bmi(52.5, 1.65))
print(bmi('0',7))
print(bmi(0,7))
print(bmi(6,'0'))
print(bmi(8,0))
print(bmi("h3llo",7))
print(bmi(5,"kil"))
print(bmi(7, 7))


#another way
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2
    
def lb_to_kg(lb):
    return lb * 0.45359237
    
def ft_and_inch_to_m(ft, inch=0.0):
    return ft * 0.3048 + inch * 0.0254

print(bmi(weight = lb_to_kg(147), height = ft_and_inch_to_m(5, 4)))
