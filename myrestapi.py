import requests


# to start the server type this in cmd , cars.json has to be the complete path:
# json-server --watch D:\e845c414d155078681778a99015e9fcff1f0c84d\cars.json
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

try:
# the full doc is requested
    # reply = requests.get("http://localhost:3000/cars")
#  one item is requested
    # reply = requests.get('http://localhost:3000/cars/8')

# The json-server assumes that a URI formed in the following way:
#
# http://server:port/resource?_sort=property
#
# causes the response to be sorted in ascending order using a property named prop.
# Note the ? character – it separates the resource identification from additional request parameters.
#     reply = requests.get('http://localhost:3000/cars?_sort=production_year')

# The json-server is also able to reverse the sort order – you just have to rewrite theURI in the following way:
#
# http://server:port/resource?_sort=property&_order=desc
#
# Note the & character – it separates additional request parameters from each other. this didn't work for me so added the client side sorting line 65-66
    reply = requests.get('http://localhost:3000/cars?_sort=production_year&_order=desc')
except requests.RequestException:
    print("Communication error")
else:
    # The server informs the client whether the connection is kept or not by using a field named Connection, placed in the response's header.
    # close means that the server is going to close the connection as soon as the response is fully transmitted (this was the server’s default behavior in HTTP 1.0).
    print('Connection=' + reply.headers['Connection'])
    if reply.status_code == requests.codes.ok:
        # print(reply.text)
        # print(reply.headers['Content-Type'])
        # print(reply.json())
        # show(reply.json())
        cars = reply.json()
        sorted_cars = sorted(cars, key=lambda x: x['production_year'], reverse=True)
        show(sorted_cars)
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print("Server error")
# json-server assumes that the data collection inherits its name from the source data file name. As we named the file cars, the server will publish the data as cars, too.
# You have to use the name in the URI unless you want to get the default (root) document, which is completely useless to us.

# Note (very important) – the fact that the json-server serves the data initially encoded as JSON has absolutely nothing to do with the fact that we will
# transmit JSON messages between the client (our code) and the server (json-server). The way the server is used to initialize and store data is actually a
# black-box for us (unless we are implementing the server itself).
# Different servers may use different means – it's none of our business when we are the clients.

# A particular server may provide some additional facilities e.g., it may manipulate data before sending it to the client. The json-server is able to sort the items using any of the properties as a sort key (by default, it sorts items by their ids).
# Usually, the URI does the trick, but remember that there is no common standard covering such additional functions – consult the server's documentation to learn more.