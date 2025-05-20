from datetime import datetime

def time_dec(function):    
    def internal_wrapper(*args):
        # get current time using now() method
        timestamp = datetime.now()
        # convert timestamp to human-readable string, following passed pattern:
        string_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        print('"{}" was called at "{}" with the following arguments:'.format(function.__name__,string_timestamp))
        print('\t{}'.format(args))
        function(*args)
        

    return internal_wrapper
    
@time_dec    
def add(*args):
    pstring = ""
    num=0
    for i in args:
        pstring += str(i)
        pstring += " + "
        num+=i
    print(pstring," = ", num)
@time_dec
def multiply(*args):
    pstring = ""
    num=1
    for i in args:
        pstring += str(i)
        pstring += " * "
        num*=i
    print(pstring," = ", num)
    
# plus = time_dec(add)
# plus(1,1)
add(1,2,3,4)
multiply(1,2,3,4)



Decorators in Python are a powerful tool that allows you to modify the behavior of a function or class without changing its source code. They provide a simple syntax for calling higher-order functions and can be used to extend the functionality of existing functions.

Basic Concept

A decorator is essentially a function that takes another function as an argument and returns a new function that adds some functionality to the original function. This is done by defining an inner function within the decorator that wraps the original function.

Example of a Simple Decorator

Here is a basic example of a decorator that prints a message before and after calling the original function:

def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = decorator(say_whee)
say_whee()
Output:

Something is happening before the function is called
Whee!
Something is happening after the function is called
In this example, the decorator function takes say_whee as an argument and returns the wrapper function, which adds additional behavior before and after calling say_whee.

Using the @ Symbol

Python provides a more elegant way to apply decorators using the @ symbol. This is equivalent to the previous example but with cleaner syntax:

def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def say_whee():
print("Whee!")

say_whee()
Output:

Something is happening before the function is called
Whee!
Something is happening after the function is called
Decorators with Arguments

Decorators can also be used with functions that take arguments. To handle this, the inner function should accept *args and **kwargs to pass any number of positional and keyword arguments to the original function.

Example

def smart_divide(func):
def wrapper(a, b):
print("I am going to divide", a, "and", b)
if b == 0:
print("Whoops! cannot divide")
return
return func(a, b)
return wrapper

@smart_divide
def divide(a, b):
return a / b

print(divide(2, 5))
print(divide(2, 0))
Output:

I am going to divide 2 and 5
0.4
I am going to divide 2 and 0
Whoops! cannot divide
None
Chaining Decorators

Multiple decorators can be applied to a single function by stacking them on top of each other. 
The decorators are applied from the bottom up.
the decorator nearest to the functions decorates it first then the ohter decorator decorates the decorated funcion
Example

def star(func):
    def wrapper(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return wrapper

def percent(func):
    def wrapper(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return wrapper

#- percent wraps printer, adding % before and after it.
#- star then wraps the modified printer, adding * before and after the percent decoration.
@star
@percent
def printer(msg):
    print(msg)

printer("Hello")
Output:

***************
%%%%%%%%%%%%%%%
Hello
%%%%%%%%%%%%%%%
***************
In this example, the printer function is first decorated with @percent and then with @star, resulting in both decorators being applied to the function.

Decorators are a versatile and powerful feature in Python that can help you write cleaner, more maintainable code by separating concerns and adding functionality to existing functions without modifying their source code.
