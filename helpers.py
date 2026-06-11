# ================================================
# helpers.py - a module to be imported
# ================================================

PI = 3.14159

def greet(name):
    """Return a friendly greeting."""
    return f"Hello, {name}!"

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def shout(text):
    """Return text in uppercase with an exclamation mark."""
    return text.upper() + "!"


# This will only print if helpers.py is run DIRECTLY
# Not when it's imported
if __name__ == "__main__":
    print("helpers.py was run directly!")
    print(greet("World"))
    print(multiply(5, 6))