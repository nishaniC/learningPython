def read_int(prompt, min, max):
    try:
        value=int(input(prompt))
        assert value<=max and value>=min
        return value
    except ValueError:
        print("Error: wrong input")
    except AssertionError:
        print("Error: the value is not within permitted range (",min,"..",max,")")
    
    return read_int(prompt, min, max)
        


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)




##############################################################################################
class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)

#################################################################
#To assign error numbers to your own exceptions in Python, you can:

#Implement __str__ to control the display of exceptions.
#Subclass your customized exception for your particular use cases.
#Use additional class attributes to provide detail without needing to pass parameters
