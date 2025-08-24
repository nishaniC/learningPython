import json
# The first JSON module's power is the ability to automatically convert Python data (not all of it and not always) into a JSON string.
# If you want to carry out such an operation, you may use a function named dumps().
electron = 1.602176620898E10-19
print(json.dumps(electron))
# 16021766189.98

comics = '"The Meaning of Life" by Monty Python\'s Flying Circus'
print(json.dumps(comics))
# "\"The Meaning of Life\" by Monty Python's Flying Circus"

my_list = [1, 2.34, True, "False", None, ['a', 0]]
print(json.dumps(my_list))
# [1, 2.34, true, "False", null, ["a", 0]]

my_tuple = (1, 2.34, True, "False", None, ['a', 0])
print(json.dumps(my_tuple))
# [1, 2.34, true, "False", null, ["a", 0]]

my_dict = {'me': "Python", 'pi': 3.141592653589, 'data': (1, 2, 4, 8), 'set': None}
print(json.dumps(my_dict))
# {"me": "Python", "pi": 3.141592653589, "data": [1, 2, 4, 8], "set": null}

#  You cannot just dump the content of an object
# There are at least two options we can make use of. The first of them is based on the fact that we can substitute the function dumps()
# uses to obtain a textual representation of its argument. There are two steps to take:
#
# write your own function knowing how to handle your objects;
# make dumps() aware of it by setting the keyword argument named default;
class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__ + ' is not JSON serializable')

# this is used in line 124
# Note: the decode_who() function receives a Python entity, or more specifically – a dictionary. As Who's constructor expects two ordinary values, a string and a number,
# not a dictionary, we have to use a little trick – we've employed the ** operator(Python’s unpacking operator
# This does the same thing as the manual version, but more concisely:
#
# **w unpacks the dictionary into keyword arguments.
#
# If w = {'name': 'Jane Doe', 'age': 23}, then Who(**w) becomes Who(name='Jane Doe', age=23).) to turn the directory into a list of keyword arguments built out of the
# dictionary's key:value pairs. Of course, the keys in the dictionary must have the same names as the constructor's parameters.
def decode_who(w):
    return Who(**w)
    # return Who(w['name'], w['age'])


some_man = Who('John Doe', 42)
print(json.dumps(some_man, default=encode_who))
# {"name": "John Doe", "age": 42}

#
# The second approach is based on the fact that the serialization is actually done by the method named default(), which is a part of the json.JSONEncoder class.
# It gives you the opportunity to overload the method defining a JSONEncoder's subclass and to pass it into dumps()
# using the keyword argument named cls –

# As you can see, we are released from the obligation to raise any exceptions.
import json


class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(self)


some_man = Who('John Doe', 42)
print(json.dumps(some_man, cls=MyEncoder))

# Note: the process in which an object (stored internally by Python) is converted into textual or any other portable aspect is often called serialization.
# Similarly, the reverse action (from portable into internal) is called deserialization.

# get a JSON string and to turn it into Python data is named loads()
#  it takes a string (hence the s at the end of its name) and tries to create a Python entity corresponding to the received data.
#  if a number encoded inside a JSON string doesn't have any fraction part, Python will create an integer number, or a float number otherwise.
jstr = '16021766189.98'
print(jstr)
# 16021766189.98
electron = json.loads(jstr)
print(type(electron))
print(electron)
# <class 'float'>
# 16021766189.98

# double backslashes inside the jstr is necessary. as we have to deliver an exact JSON string into the loads().
# This means that the backslash must precede all quotes existing within the string.
# Removing any of them will make the string invalid and loads() will not like it for sure.
jstr = '"\\"The Meaning of Life\\" by Monty Python\'s Flying Circus"'
print(jstr)
comics = json.loads(jstr)
print(type(comics))
print(comics)
# "\"The Meaning of Life\" by Monty Python's Flying Circus"
# <class 'str'>
# "The Meaning of Life" by Monty Python's Flying Circus

jstr = '[1, 2.34, true, "False", null, ["a", 0]]'
print(jstr)
# [1, 2.34, true, "False", null, ["a", 0]]
my_list = json.loads(jstr)
print(type(my_list))
print(my_list)
# <class 'list'>
# [1, 2.34, True, 'False', None, ['a', 0]]

# JSON object will be processed correctly
json_str = '{"me":"Python","pi":3.141592653589, "data":[1,2,4,8],"friend":"JSON","set": null}'
# print(json_str)
# {"me":"Python","pi":3.141592653589, "data":[1,2,4,8],"friend":"JSON","set": null}
my_dict = json.loads(json_str)
print(type(my_dict))
print(my_dict)
# <class 'dict'>
# {'me': 'Python', 'pi': 3.141592653589, 'data': [1, 2, 4, 8], 'friend': 'JSON', 'set': None}

old_man = Who("Jane Doe", 23)
json_str = json.dumps(old_man, default=encode_who)

# As you can see, there’s a keyword argument name object_hook, which is used to point to the function responsible for creating
# a brand new object of a needed class and for filling it with actual data.
# Note: the function, specified by the object_hook will be invoked only when the JSON string describes a JSON object. Sorry, there are no exceptions to this rule.
# there won’t be an error if the JSON string isn’t an object. Python’s json.loads() will still parse the string just fine;
# it simply won’t call your object_hook because there’s no object to hook into.
new_man = json.loads(json_str, object_hook=decode_who)
print(type(new_man))
print(new_man.__dict__)
# <class '__main__.Who'>
# {'name': 'Jane Doe', 'age': 23}

# As previously, a purer object approach is also possible, and is based on redefining the JSONDecoder class.
# Unfortunately, this variant is more complicated than its encoding counterpart.
# We don't need to rewrite any method, but we do have to redefine the superclass constructor, which makes our job a little more painstaking.
# The new constructor is intended to do just one trick – set a function for object creation.
class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_who)

    def decode_who(self, d):
        return Who(**d)

some_man = Who('Jane Doe', 23)
json_str = json.dumps(some_man, cls=MyEncoder)
new_man = json.loads(json_str, cls=MyDecoder)

print(type(new_man))
print(new_man.__dict__)
# <class '__main__.Who'>
# {'name': 'Jane Doe', 'age': 23}

# If you want to deserialize a list of custom objects, you can do something like this:
json_str = '[{"name": "Jane", "age": 23}, {"name": "John", "age": 30}]'
people = json.loads(json_str, object_hook=decode_who)

print(type(people))
print(people)
# <class 'list'>
# [<__main__.Who object at 0x000002A691581C70>, <__main__.Who object at 0x000002A6914318C0>]