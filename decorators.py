# ================================================
# DECORATORS (ep 35)
# Function that takes a function and returns a new function
# ================================================
import time


# ================================================
# Building up: functions are values
# ================================================
def greet():
    return "Hello!"

say_hi = greet                     # NO parens - assign the function itself
print(say_hi())                    # works - say_hi IS greet now


# ================================================
# Functions that take functions
# ================================================
def call_twice(func):
    func()
    func()


def wave():
    print("Wave!")


call_twice(wave)                   # prints "Wave!" twice


# ================================================
# Functions that return functions
# ================================================
def make_greeter():
    def inner():
        return "Hi from inner!"
    return inner                   # return the function (no parens!)


greeter = make_greeter()
print(greeter())                   # call it


# ================================================
# THE DECORATOR TEMPLATE
# Memorize this shape!
# ================================================
def my_decorator(func):            # 1. takes a function
    def wrapper(*args, **kwargs):  # 2. defines a new function
        # do something before
        result = func(*args, **kwargs)
        # do something after
        return result
    return wrapper                  # 3. returns the new function


# ================================================
# Simple decorator: print before & after
# ================================================
def announce(func):
    def wrapper(*args, **kwargs):
        print(f"📢 Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅ Done with {func.__name__}")
        return result
    return wrapper


@announce                           # this is the SHORTHAND
def add(a, b):
    return a + b


# The @ is the same as: add = announce(add)
print(add(3, 5))


# ================================================
# Timer decorator - times how long a function takes
# ================================================
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱  {func.__name__} took {end - start:.4f}s")
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(0.5)
    return "done"


slow_function()


# ================================================
# Stacking decorators
# Applied bottom-up: log first, then timer wraps that
# Same as: process = timer(log(process))
# ================================================
def log(func):
    def wrapper(*args, **kwargs):
        print(f"  → log: calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"  → log: returned {result}")
        return result
    return wrapper


@timer
@log
def process(x):
    time.sleep(0.1)
    return x * 2


process(5)


# ================================================
# Equivalent without @ syntax
# ================================================
def square(x):
    return x ** 2


# Manually wrap:
square = announce(square)
print(square(4))                   # same as @announce


# ================================================
# Practical example: require positive numbers
# Decorator that validates input
# ================================================
def require_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Negative not allowed: {arg}")
        return func(*args, **kwargs)
    return wrapper


@require_positive
def square_root(x):
    return x ** 0.5


print(square_root(16))             # works - 4.0

try:
    square_root(-9)                # raises ValueError
except ValueError as e:
    print(f"Error: {e}")


# ================================================
# Common decorators you'll see in real code:
# @property     - turn a method into a "fake attribute"
# @staticmethod - method that doesn't use self
# @classmethod  - method that takes the class, not instance
# @login_required (Django)
# @api_view (DRF)
# @cache (functools)
# @lru_cache (functools)
# ================================================


# Example: @property
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property                       # makes this look like an attribute
    def full_name(self):
        return f"{self.first} {self.last}"


p = Person("Selvi", "S")
print(p.full_name)                  # NO parentheses - looks like a property