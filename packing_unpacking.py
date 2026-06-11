# ================================================
# PACKING & UNPACKING - PRACTICE
# ================================================

# Packing in assignment - comma creates tuple
data = 1, 2, 3
print(f"Packed: {data}")            # (1, 2, 3)

# Unpacking - splits a sequence
a, b, c = data
print(f"Unpacked: {a}, {b}, {c}")   # 1, 2, 3

# Collector * during unpacking
first, *rest = [10, 20, 30, 40]
print(f"First: {first}, Rest: {rest}")     # 10, [20, 30, 40]

*head, last = [10, 20, 30, 40]
print(f"Head: {head}, Last: {last}")       # [10, 20, 30], 40

# *args in function definition - packs positional args
def total(*nums):
    print(f"Got: {nums}")           # tuple
    return sum(nums)

print(total(1, 2, 3, 4, 5))         # 15

# **kwargs in function definition - packs keyword args
def info(**details):
    print(f"Got: {details}")        # dict
    
info(name="Selvi", age=22)

# * unpacking in a function call
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))                   # 6

# ** unpacking in a function call
def greet(name, age):
    return f"{name}, {age}"

person = {"name": "Selvi", "age": 22}
print(greet(**person))              # Selvi, 22

# Combining lists with *
a = [1, 2, 3]
b = [4, 5, 6]
print([*a, *b])                     # [1, 2, 3, 4, 5, 6]

# Merging dicts with **
d1 = {"x": 1, "y": 2}
d2 = {"z": 3}
print({**d1, **d2})                 # {'x': 1, 'y': 2, 'z': 3}

# Unpacking in for loop
for k, v in {"a": 1, "b": 2}.items():
    print(f"{k} = {v}")

# Wrapper pattern - pack and forward
def wrapper(*args, **kwargs):
    print(f"Forwarding {args} and {kwargs}")
    return target(*args, **kwargs)

def target(a, b, sep="-"):
    return f"{a}{sep}{b}"

print(wrapper("hello", "world", sep="_"))   # hello_world