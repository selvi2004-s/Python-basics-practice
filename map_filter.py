# ================================================
# MAP & FILTER (eps 39, 40)
# Apply functions to entire collections
# ================================================


# ================================================
# MAP - apply a function to every item
# Returns an iterator (lazy, not a list)
# ================================================
nums = [1, 2, 3, 4, 5]


# Using a regular function
def square(x):
    return x ** 2


result = map(square, nums)
print(result)                       # <map object> - just a recipe
print(type(result))                 # <class 'map'>

# To see the values, wrap in list()
print(list(result))                 # [1, 4, 9, 16, 25]


# ================================================
# After iterating, map is empty!
# ================================================
result = map(square, nums)
print(list(result))                 # [1, 4, 9, 16, 25]
print(list(result))                 # [] - already used up


# ================================================
# Common pattern: convert immediately
# ================================================
squared = list(map(square, nums))   # do it in one line
print(squared)                       # [1, 4, 9, 16, 25]


# ================================================
# Map with lambda - very common for short operations
# ================================================
doubled = list(map(lambda x: x * 2, nums))
print(doubled)                       # [2, 4, 6, 8, 10]

# String operations
names = ["selvi", "aram", "anna"]
capitalized = list(map(str.capitalize, names))
print(capitalized)                   # ['Selvi', 'Aram', 'Anna']


# ================================================
# Map can use multiple iterables at once
# Function takes one argument per iterable
# ================================================
a = [1, 2, 3]
b = [10, 20, 30]

summed = list(map(lambda x, y: x + y, a, b))
print(summed)                        # [11, 22, 33]


# ================================================
# Map vs list comprehension
# Comprehensions are usually more Pythonic
# ================================================
doubled_map = list(map(lambda x: x * 2, nums))
doubled_comp = [x * 2 for x in nums]    # same result, cleaner
print(doubled_map == doubled_comp)       # True


# ================================================
# FILTER - keep only items where function returns True
# ================================================
nums = list(range(1, 11))           # [1..10]


# Keep only even numbers
def is_even(x):
    return x % 2 == 0


evens = list(filter(is_even, nums))
print(evens)                         # [2, 4, 6, 8, 10]


# ================================================
# Filter with lambda
# ================================================
big_nums = list(filter(lambda x: x > 5, nums))
print(big_nums)                      # [6, 7, 8, 9, 10]


# ================================================
# Filter strings - keep names with > 3 letters
# ================================================
names = ["Selvi", "Bob", "Aram", "Tim", "Anna"]
long_names = list(filter(lambda n: len(n) > 3, names))
print(long_names)                    # ['Selvi', 'Aram', 'Anna']


# ================================================
# Filter with None - keeps only "truthy" values
# Removes 0, None, "", empty lists, False
# ================================================
mixed = [1, 0, "hello", "", None, [1, 2], [], False, True]
truthy = list(filter(None, mixed))
print(truthy)                        # [1, 'hello', [1, 2], True]


# ================================================
# Filter vs list comprehension
# ================================================
evens_filter = list(filter(lambda x: x % 2 == 0, nums))
evens_comp = [x for x in nums if x % 2 == 0]    # cleaner
print(evens_filter == evens_comp)    # True


# ================================================
# Combining map and filter
# "Double all the even numbers"
# ================================================

# With map and filter (harder to read)
result1 = list(map(lambda x: x * 2,
                   filter(lambda x: x % 2 == 0, nums)))
print(result1)                       # [4, 8, 12, 16, 20]

# With list comprehension (much cleaner)
result2 = [x * 2 for x in nums if x % 2 == 0]
print(result2)                       # [4, 8, 12, 16, 20]

# This is why comprehensions are preferred in Python


# ================================================
# Real-world example - process a list of users
# ================================================
users = [
    {"name": "Selvi", "age": 22, "active": True},
    {"name": "Aram", "age": 17, "active": True},
    {"name": "Anna", "age": 30, "active": False},
    {"name": "Bob",  "age": 25, "active": True},
]

# Get names of active adult users
active_adults = list(
    filter(lambda u: u["active"] and u["age"] >= 18, users)
)
print("Active adults:")
for u in active_adults:
    print(f"  {u['name']}")

# Same thing with comprehension - much nicer
names = [u["name"] for u in users
         if u["active"] and u["age"] >= 18]
print(f"\nNames only: {names}")


# ================================================
# Map on dict values
# ================================================
prices = {"apple": 100, "banana": 50, "cherry": 200}

# Apply 10% discount to each price
discounted = {item: price * 0.9 for item, price in prices.items()}
print(discounted)


# ================================================
# Quick reference
# ================================================
# map(func, iterable)    - transform each item
# filter(func, iterable) - keep items where func returns True
# Both return iterators (use list() to materialize)
# 
# Equivalent list comprehensions:
# map(f, items)        →  [f(x) for x in items]
# filter(p, items)     →  [x for x in items if p(x)]
# map + filter         →  [f(x) for x in items if p(x)]
# 
# Use comprehensions for clarity; map/filter when you
# already have a function defined.