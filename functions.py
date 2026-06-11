# Functions

# Parameter: names listed in the functions defintions
# Argument: real values passed to the function


# Define a function
def test():
    print("This is a function")


# Define a function with parameters and return a value
def sqft(w, h):
    v = w * h
    return v


# Call a function

print(sqft(5, 10))

# Call a function multiple times
for i in range(3):
    test()

# Functions and scops
# can use sth from bigger scope but cant do the reverse

# Gloval scope
name = "Selvi"

#Functions can access the global scope 
def test1():
    print(f'My name is {name}')

test1()

#Global scope cant access function scope 
x=10 # this is in global scope
def test2():
    x=50
    print(f'Function scope: {x}')

test2()
print(f'Global scope: {x}')

#Global > function > statement 
x= 15# this is in global scope

def test3():
    x=0
    print(f'Function scope: {x}')
    for i in range(3):
     x+=1
     y=x*i
     print(f'Statement x: {x}')
     print(f'Statement y: {y}')



test3()
print(f'Global scope: {x}')


# ================================================
# PYTHON FUNCTIONS - PRACTICE
# ================================================


# Basic function
# Takes input, returns output
def greet(name):
    return f"Hello, {name}!"

print(greet("Selvi"))  # Calling the function


# Function with no return - returns None automatically
def say_hi():
    print("Hi!")

result = say_hi()
print(f"Return value: {result}")  # None

say_hi()


# ================================================
# Default parameters
# If user doesn't give a value, use the default
# ================================================
def introduce(name, age=18, city="Yerevan"):
    return f"{name}, {age}, from {city}"

print(introduce("Selvi"))                        # Uses both defaults
print(introduce("Aram", 25))                     # Uses default city
print(introduce("Anna", 23, "Gyumri"))           # No defaults used


# ================================================
# Keyword arguments
# Calling with name=value lets you reorder , but function prints as it orders you just give arguments in dif order 
# ================================================
print(introduce(city="Paris", name="David", age=30))


# ================================================
# Returning multiple values (really a tuple)
# ================================================
def get_min_max(nums):
    return (min(nums), max(nums))   # Returns a tuple

low, high = get_min_max([3, 7, 1, 9, 4])         # Unpacking into 2 variables
print(f"Min: {low}, Max: {high}")


# ================================================
# *args - accept any number of positional arguments
# Inside the function, args is a tuple
# ================================================
def total(*nums):
    print(f"Got args: {nums}")    # Show what we received
    return sum(nums)

print(total(1, 2, 3))             # 6
print(total(10, 20, 30, 40, 50))  # 150
print(total())                    # 0


# ================================================
# **kwargs - accept any number of keyword arguments
# Inside the function, kwargs is a dict
# ================================================
def describe(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

describe(name="Selvi", age=22, city="Yerevan", job="intern")


# ================================================
# Mixing everything: positional, default, *args, **kwargs
# Order matters in the signature!
# ================================================
def full_example(required, default="x", *args, **kwargs):
    print(f"Required: {required}")
    print(f"Default:  {default}")
    print(f"Args:     {args}")
    print(f"Kwargs:   {kwargs}")

full_example("a", "b", 1, 2, 3, key1="v1", key2="v2")


# ================================================
# Unpacking when CALLING a function
# * unpacks a list/tuple, ** unpacks a dict
# ================================================
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))                 # Same as add(1, 2, 3)

info = {"a": 10, "b": 20, "c": 30}
print(add(**info))                # Same as add(a=10, b=20, c=30)


# ================================================
# Scope - local vs global variables
# Variables inside a function don't leak outside
# ================================================
def func():
    x = 10        # Local to func
    print(f"Inside func: x = {x}")

func()
# print(x)   # Would error - x doesn't exist out here


# ================================================
# Global keyword
# Needed when you want to MODIFY a global from inside
# ================================================
count = 0

def increment():
    global count        # Tell Python: use the global one
    count += 1

increment()
increment()
increment()
print(f"Count after 3 increments: {count}")  # 3


# ================================================
# Mutable default argument - the famous trap!
# DON'T use lists/dicts as default values directly
# ================================================
def bad_add(item, lst=[]):        # Bad - shared across calls
    lst.append(item)
    return lst

print(bad_add("a"))               # ['a']
print(bad_add("b"))               # ['a', 'b']  WEIRD - keeps growing!

def good_add(item, lst=None):     # Good - safe pattern
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(good_add("a"))              # ['a']
print(good_add("b"))              # ['b']  Fresh each call


# ================================================
# Pass by reference of value - mutating vs rebinding
# ================================================
def mutate(lst):
    lst.append(99)                # Changes the actual list

def rebind(lst):
    lst = [1, 2, 3]               # Just moves the local label

x = [1, 2]
mutate(x)
print(f"After mutate: {x}")       # [1, 2, 99] - changed

y = [1, 2]
rebind(y)
print(f"After rebind: {y}")       # [1, 2] - unchanged


# ================================================
# Lambda - anonymous one-line function
# Useful when passing as argument
# ================================================
square = lambda x: x * x          # Assigned, but def is preferred for this
print(f"Square of 5: {square(5)}")

# More common use - inline with sorted, map, filter
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(nums, key=lambda x: -x))   # Sort descending


# ================================================
# Functions are first-class objects
# Pass them around like any value
# ================================================
def double(x): return x * 2
def triple(x): return x * 3

operations = [double, triple, lambda x: x + 100]   # List of functions!
for op in operations:
    print(op(5))                  # 10, 15, 105


def apply(func, value):           # Function takes another function
    return func(value)

print(apply(double, 7))           # 14
print(apply(lambda x: x ** 2, 7)) # 49


# ================================================
# Docstrings - documentation inside the function
# Triple-quoted string as first line
# ================================================
def calculate_tax(income, rate=0.2):
    """
    Calculate tax for given income.
    
    Args:
        income: gross income
        rate: tax rate (default 0.2)
    Returns:
        tax amount
    """
    return income * rate

print(calculate_tax(1000))
print(calculate_tax.__doc__)      # Access the docstring
# help(calculate_tax)             # Uncomment for nicely formatted help


# ================================================
# Type hints - optional, just for clarity
# Python doesn't enforce them, but they help VS Code
# ================================================
def greet_typed(name: str, age: int = 0) -> str:
    return f"{name} is {age}"

print(greet_typed("Selvi", 22))


# ================================================
# Nested functions and closures
# Inner function "remembers" the outer variable
# ================================================
def make_multiplier(factor):
    def multiply(x):
        return x * factor          # Uses 'factor' from outer scope
    return multiply

double_fn = make_multiplier(2)
triple_fn = make_multiplier(3)
print(double_fn(5))                # 10
print(triple_fn(5))                # 15


# ================================================
# Realistic combined example
# Uses *args, **kwargs, default, docstring, dict, return
# ================================================
def process_users(*users, role="member", **extra_attrs):
    """Build a list of user dicts with role and any extra attributes."""
    result = []
    for name in users:
        user = {"name": name, "role": role}
        user.update(extra_attrs)
        result.append(user)
    return result


users = process_users(
    "Selvi", "Aram", "Anna",
    role="admin",
    department="engineering",
    active=True
)

for u in users:
    print(u)