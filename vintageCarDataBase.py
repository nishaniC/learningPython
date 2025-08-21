from os import system

import requests
import json

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]
h_content = {'Content-Type': 'application/json'}
h_close = {'Connection': 'Close'}
BASE_URL = "http://localhost:3000/cars"

def check_server(cid=None):
    # returns True or False;
    # when invoked without arguments simply checks if server responds;
    # invoked with car ID checks if the ID is present in the database;
    if cid is None:
        try:
            reply = requests.head(BASE_URL, timeout=1)
            if requests.codes.ok == reply.status_code:
                return True
        except requests.exceptions.Timeout:
            return False
    else:
        try:
            reply = requests.get(f"{BASE_URL}/{cid}", timeout=1)
        except requests.exceptions.Timeout:
            return False
        else:
            if requests.codes.ok == reply.status_code:
                return True
            else:
                return False

def print_menu():
    # prints user menu - nothing else happens here;
    print("+---------------------------------+")
    print("|      Vintage Cars Database      |")
    print("+---------------------------------+")
    print("MENU")
    print("=======")
    print("1. List cars")
    print("2. Add new car")
    print("3. Delete car")
    print("4. Update car")
    print("0. Exit")

def read_user_choice():
    # reads user choice and checks if it's valid;
    # returns '0', '1', '2', '3' or '4'
    user_input=input("Enter your choice: ")
    if user_input in ['0', '1', '2', '3','4']:
        return user_input
    else:
        return None

def print_header():
    # prints elegant cars table header;
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()

def print_car(car):
    # prints one car's data in a way that fits the header;
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()

def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()

def list_cars():
    # gets all cars' data from server and prints it;
    # if the database is empty prints diagnostic message instead;

    print_header()
    reply=requests.get('http://localhost:3000/cars/', timeout=1)
    # print(reply.json())
    for car in reply.json():
        print_car(car)


def name_is_valid(name):
    # checks if name (brand or model) is valid;
    # valid name is non-empty string containing
    # digits, letters and spaces;
    # returns True or False;
    if name is not None and name != '' and name != ' ':
        return True
    else:
        return False


def enter_id():
# allows user to enter car's ID and checks if it's valid;
# valid ID consists of digits only;
# returns int or None (if user enters an empty line);
    try:
        cid = int(input("Enter car id(digits only): ").strip())
        return cid
    except Exception as e:
        print(f"Error: {e}")
        return None

def enter_production_year():
    # allows user to enter car's production year and checks if it's valid;
    # valid production year is an int from range 1900..2000;
    # returns int or None  (if user enters an empty line);
    try:
        prodyear = int(input("Enter production year: "))
        if 1900 <= prodyear <= 2100:
            return prodyear
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def enter_name(what):
    # allows user to enter car's name (brand or model) and checks if it's valid;
    # uses name_is_valid() to check the entered name;
    # returns string or None  (if user enters an empty line);
    # argument describes which of two names is entered currently ('brand' or 'model');
    if what == 'brand':
        brand = input("Enter brand: ")
        if name_is_valid(brand):
            return brand
    elif what == 'model':
        model = input("Enter model: ")
        if name_is_valid(model):
            return model
    return None


def enter_convertible():
    # allows user to enter Yes/No answer determining if the car is convertible;
    # returns True, False or None  (if user enters an empty line);
    convertible = input("Enter convertible? [y/n] (empty string to exit): ")
    if convertible.lower() == 'y':
        return True
    elif convertible.lower() == 'n':
        return False
    return None

def delete_car():
    # asks user for car's ID and tries to delete it from database;
    carid=enter_id()
    if not check_server(carid):
        print("Car ID not found.")
        return
    try:
        reply = requests.delete(f"{BASE_URL}/{carid}", timeout=10)
        # f"{BASE_URL}/{car_id}"
        # if the server responded with 200 it means “okay”
        print("res=" + str(reply.status_code))
    except requests.RequestException:
        print('Communication error')


def input_car_data(with_id):
    # lets user enter car data;
    # argument determines if the car's ID is entered (True) or not (False);
    # returns None if user cancels the operation or a dictionary of the following structure:
    # {'id': int, 'brand': str, 'model': str, 'production_year': int, 'convertible': bool }
    brand = enter_name('brand')
    model = enter_name('model')
    production_year = enter_production_year()
    convertible = enter_convertible()
    if brand is None or model is None or production_year is None or convertible is None:
        return None
    if with_id:
        carid = enter_id()
        if(carid is None):
            return None
        return {'id':carid, 'brand': brand, 'model': model, 'production_year': production_year, 'convertible': convertible}
    else:
        return {'brand': brand, 'model': model, 'production_year': production_year, 'convertible': convertible }


def add_car():
    # invokes input_car_data(True) to gather car's info and adds it to the database;
    new_car=input_car_data(True)
    try:
        # this is where the most important things happen – we invoke the post() function (note the URI – it just points to the resource, not the particular item)
        # and set two additional parameters: one (headers) to complement the request header with the Content-Type field, and the second (data) to pass the JSON message to the request.
        reply = requests.post('http://localhost:3000/cars', headers=h_content, data=json.dumps(new_car))
        # Note the server's status code – it's 201 ("created").
        # print("reply=" + str(reply.status_code))
    except requests.RequestException:
        print('Communication error')


def update_car():
    # invokes enter_id() to get car's ID if the ID is present in the database;
    # invokes input_car_data(False) to gather new car's info and updates the database;
    carid=enter_id()
    if (carid is not None) and check_server(carid):
        car = input_car_data(False)
    else:
        print("Invalid carid")
        return
    try:
        # note – we have to make a URI that clearly indicates the item being modified; moreover, we must send the complete item, not only the changed property.
        reply = requests.put(f"{BASE_URL}/{carid}", headers=h_content, data=json.dumps(car))
        # print("reply=" + str(reply.status_code))

    except requests.RequestException:
        print('Communication error')


while True:
    if not check_server():
        print("Server is not responding - quitting!")
        exit(1)
    print_menu()
    choice = read_user_choice()
    if choice == '0':
        print("Bye!")
        exit(0)
    elif choice == '1':
        list_cars()
    elif choice == '2':
        add_car()
    elif choice == '3':
        delete_car()
    elif choice == '4':
        update_car()
