# ================================================
# INHERITANCE & MULTIPLE INHERITANCE (eps 31, 32)
# ================================================


# ================================================
# Parent class (also called "base" or "super")
# ================================================
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

    def describe(self):
        return f"This is {self.name}"


# ================================================
# Child class - inherits everything from Animal
# class ChildName(ParentName):
# ================================================
class Cat(Animal):
    # New method, specific to Cat
    def purr(self):
        return f"{self.name} purrs"


c = Cat("Whiskers")
print(c.speak())                   # inherited from Animal
print(c.describe())                # inherited
print(c.purr())                    # unique to Cat


# ================================================
# Overriding parent methods
# ================================================
class Dog(Animal):
    def speak(self):               # override - replaces parent's speak
        return f"{self.name} barks!"


d = Dog("Rex")
print(d.speak())                   # uses Dog's version - "Rex barks!"


# ================================================
# super() - call the parent's version
# Used in __init__ to keep parent's setup
# ================================================
class Puppy(Dog):
    def __init__(self, name, age):
        super().__init__(name)     # call Dog/Animal's __init__
        self.age = age              # add new attribute

    def describe(self):
        # call parent's describe, then add to it
        parent_text = super().describe()
        return f"{parent_text}, age {self.age}"


p = Puppy("Buddy", 1)
print(p.speak())                   # inherited from Dog
print(p.describe())                # custom but uses parent's text


# ================================================
# isinstance() - check if object belongs to a class
# ================================================
print(isinstance(p, Puppy))        # True - it IS a Puppy
print(isinstance(p, Dog))          # True - Puppy inherits from Dog
print(isinstance(p, Animal))       # True - all the way up the chain
print(isinstance(p, Cat))          # False - Cat is a sibling, not parent


# ================================================
# MULTIPLE INHERITANCE (ep 32)
# A class can inherit from more than one parent
# ================================================
class Flyer:
    def fly(self):
        return f"{self.name} flies"


class Swimmer:
    def swim(self):
        return f"{self.name} swims"


class Duck(Flyer, Swimmer):        # inherits from BOTH
    def __init__(self, name):
        self.name = name


donald = Duck("Donald")
print(donald.fly())                # from Flyer
print(donald.swim())               # from Swimmer


# ================================================
# Method Resolution Order (MRO)
# When two parents have the same method, Python checks
# left-to-right (the order that we wrote parents)
# ================================================
class A:
    def greet(self):
        return "Hello from A"


class B:
    def greet(self):
        return "Hello from B"


class C(A, B):                     # A comes first
    pass


c = C()
print(c.greet())                   # "Hello from A" - left wins
print(C.__mro__)                   # see the lookup order


# ================================================
# Mixin pattern - small classes added for behavior
# Common in Django for adding features to views
# ================================================
class JSONExportMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)


class TimestampMixin:
    def get_timestamp(self):
        import datetime
        return datetime.datetime.now().isoformat()


class User(JSONExportMixin, TimestampMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email


u = User("Selvi", "s@example.com")
print(u.to_json())                 # from JSONExportMixin
print(u.get_timestamp())           # from TimestampMixin