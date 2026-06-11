# ================================================
# THE UNDERSCORE - All 5 uses (ep 34)
# ================================================


# ================================================
# Use 1: _ as a "throwaway" variable
# Means "I don't care about this value"
# ================================================

# In a loop where you don't need the counter
for _ in range(3):
    print("hello")

# Unpacking and ignoring some values
x, _, z = (1, 2, 3)
print(x, z)                        # 1 3 (middle ignored)

# Ignore the rest with *_
first, *_ = [10, 20, 30, 40, 50]
print(first)                       # 10

# Multiple throwaways
_, _, important = ("ignore", "ignore", "use me")
print(important)


# ================================================
# Use 2: _name (single leading underscore)
# Convention: "this is private, don't use from outside"
# Not enforced - just a polite signal
# ================================================
class BankAccount:
    def __init__(self):
        self._balance = 0           # underscore = "internal use"

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance


account = BankAccount()
account.deposit(100)
print(account.get_balance())        # 100 - proper way

# You CAN still access _balance from outside, but you shouldn't
print(account._balance)             # works, but breaks convention


# ================================================
# Use 3: __name (double leading underscore)
# Name mangling - Python renames it for "stronger privacy"
# Used to avoid name clashes in inheritance
# ================================================
class Secret:
    def __init__(self):
        self.__hidden = "shhh"      # gets renamed to _Secret__hidden

    def reveal(self):
        return self.__hidden


s = Secret()
print(s.reveal())                   # works fine

# Direct access fails
try:
    print(s.__hidden)
except AttributeError as e:
    print(f"Can't access: {e}")

# It's actually stored under a different name
print(s._Secret__hidden)            # works but ugly - don't use this


# ================================================
# Use 4: __name__ (dunder - double on BOTH sides)
# Python's reserved special names
# These trigger special Python behavior
# ================================================
class Person:
    def __init__(self, name):       # dunder method - constructor
        self.name = name

    def __str__(self):              # dunder - how to print
        return f"Person({self.name})"

    def __len__(self):              # dunder - makes len() work
        return len(self.name)

    def __eq__(self, other):        # dunder - makes == work
        return self.name == other.name


p1 = Person("Selvi")
p2 = Person("Selvi")
p3 = Person("Aram")

print(p1)                           # uses __str__
print(len(p1))                      # uses __len__ - 5
print(p1 == p2)                     # uses __eq__ - True
print(p1 == p3)                     # False


# ================================================
# Use 5: name_ (trailing underscore)
# Avoid conflicts with Python's reserved words
# ================================================

# 'class' is a reserved keyword in Python, so use class_
def categorize(class_, value):
    return f"{class_}: {value}"


print(categorize("animal", "dog"))

# 'type' is a built-in - use type_ to avoid shadowing it
def make_item(name, type_):
    return {"name": name, "type": type_}


print(make_item("apple", "fruit"))


# ================================================
# Summary - quick reference
# ================================================
# _          → throwaway "I don't care"
# _name      → private by convention (use public methods)
# __name     → name-mangled, harder to access
# __name__   → Python's reserved special names (dunders)
# name_      → avoid clash with reserved words