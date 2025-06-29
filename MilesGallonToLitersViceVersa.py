# 1 American mile = 1609.344 metres;
# 1 American gallon = 3.785411784 litres.
def liters_100km_to_miles_gallon(liters):
    # galoons for 100000m= liters/3.785411784
    # galoons for 1m =(liters/3.785411784)/100000
    # galoons for 1609.344 metres = ((liters/3.785411784)/100000)*1609.344
    return 1/(((liters/3.785411784)/100000)*1609.344)
       
def miles_gallon_to_liters_100km(miles):
    # meters for 3.785411784 litres = miles*1609.344
    # 100kms for 3.785411784 litres = (miles*1609.344)/100000
    # 100kms for 1 litre=((miles*1609.344)/100000)/3.785411784
    return 1/(((miles*1609.344)/100000)/3.785411784)



 
 
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
print(liters_100km_to_miles_gallon(1))
print(miles_gallon_to_liters_100km(1))
