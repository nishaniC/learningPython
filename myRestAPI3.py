import json
import requests

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()


h_close = {'Connection': 'Close'}

#  if we’re going to send anything to the server, the server must be aware of what it actually is; as you already know,
#  the server informs us about the type of the contents using the Content-Type field; we can use the same technique to warn the server that we’re sending something more than a bare request.
#  This is why we prepare our Content-Type field with the appropriate value;
h_content = {'Content-Type': 'application/json'}

# This is our new car! We prepared all the data needed and packed it inside a Python dictionary – of course, we'll convert it into JSON before we send it out into the world;
new_car = {'id': 8,
           'brand': 'Porsche',
           'model': '911',
           'production_year': 1963,
           'convertible': False}

car = {'id': 6,
       'brand': 'Mercedes Benz',
       'model': '300SL',
       'production_year': 1977,
       'convertible': True}
print(json.dumps(new_car))
try:
    # this is where the most important things happen – we invoke the post() function (note the URI – it just points to the resource, not the particular item)
    # and set two additional parameters: one (headers) to complement the request header with the Content-Type field, and the second (data) to pass the JSON message to the request.
    reply = requests.post('http://localhost:3000/cars', headers=h_content, data=json.dumps(new_car))
    # Note the server's status code – it's 201 ("created").
    print("reply=" + str(reply.status_code))

    # note – we have to make a URI that clearly indicates the item being modified; moreover, we must send the complete item, not only the changed property.
    reply = requests.put('http://localhost:3000/cars/6', headers=h_content, data=json.dumps(car))
    print("reply=" + str(reply.status_code))
    reply = requests.get('http://localhost:3000/cars/', headers=h_close)
except requests.RequestException:
    print('Communication error')
else:
    print('Connection=' + reply.headers['Connection'])
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')
