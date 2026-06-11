# ================================================
# CLASSES - BASICS (ep 30)
# How to define a class, attributes, methods
# ================================================


# ================================================
# Defining a class
# class name with capital letter (convention)
# ================================================
class Dog:
    # Class variable - shared by ALL instances
    species = "Canis familiaris"

    # Constructor - runs when you create a new Dog
    def __init__(self, name, breed):
        self.name = name           # instance variable - unique per dog
        self.breed = breed

    # Method - takes self as first argument
    def bark(self):
        return f"{self.name} says woof!"

    # __str__ controls how the object is printed
    def __str__(self):
        return f"Dog(name={self.name}, breed={self.breed})"


# ================================================
# Creating instances
# ================================================
d1 = Dog("Rex", "Labrador")
d2 = Dog("Bella", "Poodle")

# Access attributes
print(d1.name)                 # Rex
print(d2.breed)                # Poodle

# Call methods
print(d1.bark())               # Rex says woof!
print(d2.bark())               # Bella says woof!

# Print uses __str__
print(d1)                      # Dog(name=Rex, breed=Labrador)

# Class variable is shared
print(d1.species)              # Canis familiaris
print(d2.species)              # Canis familiaris


# ================================================
# Modifying attributes
# Just assign to them - no setters/getters needed
# ================================================
d1.name = "Max"
print(d1.bark())               # Max says woof!


# ================================================
# Adding methods that DO things
# ================================================
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def __str__(self):
        return f"Counter: {self.count}"


c = Counter()
c.increment()
c.increment()
c.increment()
print(c)                       # Counter: 3
c.reset()
print(c)                       # Counter: 0


# ================================================
# A more realistic example
# ================================================
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Not enough money. Balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def __str__(self):
        return f"{self.owner}'s account: ${self.balance}"


account = BankAccount("Selvi", 100)
print(account)
account.deposit(50)
account.withdraw(30)
account.withdraw(500)          # too much - rejected