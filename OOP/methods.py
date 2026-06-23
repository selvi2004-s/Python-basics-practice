class Pizza:
    total_pizzas_made = 0             # class variable
    
    def __init__(self, size):
        self.size = size              # instance variable
        Pizza.total_pizzas_made += 1
    
    # INSTANCE method - needs a specific pizza
    def describe(self):
        return f"A {self.size} inch pizza"
    
    # CLASS method - works with the class, alternative constructor
    @classmethod
    def make_large(cls):
        return cls(16)                # creates a 16-inch pizza
    
    # STATIC method - just a helper, no self or cls
    @staticmethod
    def is_valid_size(size):
        return 8 <= size <= 20


# Instance method - needs an object
p = Pizza(12)
print(p.describe())                   # "A 12 inch pizza"

# Class method - called on the class, returns a new object
large = Pizza.make_large()
print(large.describe())               # "A 16 inch pizza"

# Static method - called on the class, just computes
print(Pizza.is_valid_size(14))        # True
print(Pizza.is_valid_size(50))        # False

# Class variable
print(Pizza.total_pizzas_made)        # 2