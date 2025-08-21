class Vehicle:
    def __init__(self, rn, yop, passengeryn, vehiclemass):
        self.rn = rn
        self.yop = yop
        self.passengeryn = passengeryn
        self.vehiclemass = vehiclemass

import json

class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Vehicle):
            return w.__dict__
        else:
            return super().default(self)

class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_who)

    def decode_who(self, d):
        return Vehicle(**d)
goon = True
while goon:
    print("What can I do for you?")
    print ("1 - produce a JSON string describing a vehicle")
    print("2 - decode a JSON string describing a vehicle")
    print("3 - exit")
    try:
        yc = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input")
        exit(1)

    if yc == 1:
        try:
            reg_num = str(input("Enter registration number: "))
            yearop = int(input("Enter year of production: "))
            passenger = bool(input("Enter passengery (y/n): "))
            vehiclemass = float(input("Enter vehicle mass: "))
        except ValueError:
            print("Invalid input")
            exit(1)
        v = Vehicle(reg_num, yearop, passenger, vehiclemass)
        print(json.dumps(v, cls=MyEncoder))
    if yc == 2:
        jason_string = input("Enter JASON string: ")
        print((json.loads(jason_string, cls=MyDecoder).__dict__))
    if yc == 3:
        goon = False