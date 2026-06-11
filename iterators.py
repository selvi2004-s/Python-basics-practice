# ================================================
# ITERATORS & GENERATORS (ep 36)
# How for loops actually work, and how to make your own
# ================================================


# ================================================
# THE IDEA: an iterator gives you values one at a time
# Instead of storing all values in memory like a list
# ================================================

# A list HAS all its values stored
my_list = [10, 20, 30]
print(my_list)               # [10, 20, 30] - all there

# An iterator PRODUCES values when asked
my_iter = iter(my_list)      # iter() makes an iterator from any iterable
print(my_iter)               # <list_iterator object at ...> - just a recipe


# ================================================
# next() - ask the iterator for the next value
# ================================================
nums = [10, 20, 30]
it = iter(nums)

print(next(it))              # 10
print(next(it))              # 20
print(next(it))              # 30

# One more call would raise StopIteration:
try:
    print(next(it))
except StopIteration:
    print("Iterator is exhausted (empty)")


# ================================================
# What a for loop does behind the scenes
# These two are EQUIVALENT
# ================================================
print("\nUsing for loop:")
for n in [1, 2, 3]:
    print(n)

print("\nManually (what Python does for you):")
it = iter([1, 2, 3])
while True:
    try:
        n = next(it)
        print(n)
    except StopIteration:
        break


# ================================================
# Iterators get "used up" - they only go forward
# ================================================
nums = [1, 2, 3]
it = iter(nums)

for n in it:                 # consume all values
    print(n)                 # 1, 2, 3

# Try again - empty!
print("After first loop:")
for n in it:
    print(n)                 # nothing prints - iterator is exhausted


# ================================================
# Lists are reusable - iterators are one-shot
# ================================================
nums = [1, 2, 3]

# A list can be looped many times
for n in nums:
    print(f"First pass: {n}")

for n in nums:
    print(f"Second pass: {n}")  # still works fine


# ================================================
# GENERATORS - the EASY way to make iterators
# A function with `yield` instead of `return`
# ================================================
def count_up_to(n):
    i = 1
    while i <= n:
        yield i              # produce a value, then PAUSE
        i += 1               # resume here on next next() call


# Use like any iterable
for num in count_up_to(5):
    print(f"Got: {num}")


# ================================================
# How yield works - the function PAUSES, not exits
# ================================================
def my_generator():
    print("  Started")
    yield 1
    print("  After first yield")
    yield 2
    print("  After second yield")
    yield 3
    print("  Finished")


gen = my_generator()         # NOTHING runs yet - just creates the generator
print("Generator created\n")

print(next(gen))             # runs until first yield
print(next(gen))             # resumes, runs until second yield
print(next(gen))             # resumes, runs until third yield


# ================================================
# Why generators are powerful - lazy evaluation
# Only computes values you actually ask for
# ================================================

# This would be impossible with a list (infinite memory!)
def naturals():
    n = 1
    while True:              # forever!
        yield n
        n += 1


gen = naturals()
for _ in range(5):
    print(next(gen))         # 1, 2, 3, 4, 5

# We could keep going forever, but we choose to stop


# ================================================
# Generator vs list - memory difference
# ================================================

# List approach: stores ALL million values in memory
big_list = [x * x for x in range(1_000_000)]
print(f"List has {len(big_list)} items")

# Generator approach: produces them one at a time
def big_gen():
    for x in range(1_000_000):
        yield x * x

gen = big_gen()
# Only the next value exists in memory at any time


# ================================================
# Practical example - reading huge file line by line
# is essentially using an iterator
# ================================================
# This works for any file size, even 100GB:
# with open("huge.log") as f:
#     for line in f:           # f is an iterator!
#         process(line)


# ================================================
# Generators with early stop
# ================================================
def first_n_even_numbers(n):
    count = 0
    num = 0
    while count < n:
        yield num
        num += 2
        count += 1


for x in first_n_even_numbers(5):
    print(x)                 # 0, 2, 4, 6, 8


# ================================================
# Generator expression - inline generator
# Like a list comprehension but with () instead of []
# ================================================
squares_list = [x*x for x in range(5)]      # list - stored in memory
print(squares_list)                          # [0, 1, 4, 9, 16]

squares_gen = (x*x for x in range(5))       # generator - lazy
print(squares_gen)                           # <generator object ...>

# Use it
for s in squares_gen:
    print(s)                 # 0, 1, 4, 9, 16


# ================================================
# When to use what
# - List:      need all values, will reuse, small data
# - Generator: large/infinite data, used once, memory matters
# - Iterator:  almost never make manually - use generators
# ================================================