#This class is used to demonstrate the use of Decorator functions in Python
# Decorator functions are used to add some functionality to the existing function without modifying it

#Decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def pre_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
    return wrapper

def post_decorator(func):
    def wrapper():
        func()
        print("Something is happening after the function is called.")
    return wrapper

#Function to be decorated
@my_decorator
def say_hello():
    print("Hello!")

say_hello()

@pre_decorator
def say_hello():
    print("Hello!")

say_hello()

@post_decorator
def say_hello():
    print("Hello!")

say_hello()

#Decorator function with arguments
def my_decorator_withargs(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator_withargs
def multiply(a, b):
    print("reached Here!")
    print(a * b)

tuple = (2, 3)
dict = {'a': 2, 'b': 3}

my_decorator_withargs(multiply)(tuple[0], tuple[1])

my_decorator_withargs(multiply)(**dict)