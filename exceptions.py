# ================================================
# EXCEPTIONS - try/except/else/finally (ep 37)
# How to handle errors without crashing
# ================================================


# ================================================
# THE PROBLEM: errors crash your program
# Uncomment to see the crash:
# x = 10 / 0
# print("This never runs")
# ================================================


# ================================================
# Basic try/except - catch the error
# ================================================
try:
    x = 10 / 0               # this raises an exception
except ZeroDivisionError:
    print("Caught: can't divide by zero")

print("Program continues normally!\n")


# ================================================
# Capturing the exception object with 'as'
# Lets you see the error message
# ================================================
try:
    int("hello")
except ValueError as e:
    print(f"ValueError: {e}")


# ================================================
# Multiple except blocks - one for each error type
# Python uses the FIRST matching one
# ================================================
def safe_parse(s):
    try:
        return int(s)
    except ValueError:
        print(f"  '{s}' isn't a valid number")
        return None
    except TypeError:
        print(f"  '{s}' has wrong type")
        return None


print(safe_parse("42"))      # works - returns 42
print(safe_parse("hello"))   # ValueError - returns None
print(safe_parse(None))      # TypeError - returns None


# ================================================
# Catch multiple exception types in one block
# ================================================
def safe_parse2(s):
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print(f"  Failed: {e}")
        return None


safe_parse2("oops")
safe_parse2(None)


# ================================================
# Generic Exception - catches ANYTHING
# Use carefully - can hide real bugs
# ================================================
try:
    result = 1 / 0
except Exception as e:
    print(f"Something failed: {type(e).__name__}: {e}")


# ================================================
# else - runs only if NO exception happened
# Separates "the risky part" from "what to do on success"
# ================================================
def parse_with_else(s):
    try:
        num = int(s)
    except ValueError:
        print(f"Failed to parse '{s}'")
    else:
        # only runs if try succeeded
        print(f"Got: {num}")


parse_with_else("100")       # success - else runs
parse_with_else("oops")      # failure - else skipped


# ================================================
# finally - ALWAYS runs, no matter what
# Used for cleanup
# ================================================
try:
    x = 10 / 2
    print(f"x = {x}")
except ZeroDivisionError:
    print("Division failed")
finally:
    print("This ALWAYS runs (cleanup)")

print()

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Division failed")
finally:
    print("This ALWAYS runs (cleanup)")


# ================================================
# Full structure: try / except / else / finally
# ================================================
def divide(a, b):
    print(f"\nTrying {a}/{b}...")
    try:
        result = a / b
    except ZeroDivisionError:
        print("  Can't divide by zero")
        return None
    else:
        print(f"  Success: {result}")
        return result
    finally:
        print("  (Done with division attempt)")


divide(10, 2)
divide(10, 0)


# ================================================
# raise - manually trigger an exception
# Use to signal errors from your own code
# ================================================
def withdraw(balance, amount):
    if amount < 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError(f"Not enough money. Balance: {balance}")
    return balance - amount


try:
    withdraw(100, -10)
except ValueError as e:
    print(f"\nCaught: {e}")


try:
    withdraw(100, 500)
except ValueError as e:
    print(f"Caught: {e}")


# ================================================
# Custom exception classes
# Just inherit from Exception
# ================================================
class InsufficientFundsError(Exception):
    pass                     # no body needed - just a name


class InvalidAmountError(Exception):
    pass


def withdraw_strict(balance, amount):
    if amount < 0:
        raise InvalidAmountError(f"Amount {amount} is invalid")
    if amount > balance:
        raise InsufficientFundsError(
            f"Need {amount}, only have {balance}"
        )
    return balance - amount


# Now we can catch specific custom errors
try:
    withdraw_strict(50, 100)
except InsufficientFundsError as e:
    print(f"\nNeed more money: {e}")
except InvalidAmountError as e:
    print(f"Bad amount: {e}")


# ================================================
# Common built-in exceptions you'll meet
# ================================================
errors_to_try = [
    lambda: int("abc"),              # ValueError
    lambda: "abc" + 5,               # TypeError
    lambda: [1, 2][10],              # IndexError
    lambda: {"a": 1}["missing"],     # KeyError
    lambda: 10 / 0,                  # ZeroDivisionError
    lambda: open("nope.txt"),        # FileNotFoundError
]

print("\nCommon exceptions:")
for f in errors_to_try:
    try:
        f()
    except Exception as e:
        print(f"  {type(e).__name__}: {e}")


# ================================================
# Real-world example: safely reading JSON
# ================================================
import json


def load_config(path):
    try:
        with open(path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"\n{path} doesn't exist - using defaults")
        return {}
    except json.JSONDecodeError as e:
        print(f"{path} is corrupt: {e}")
        return {}
    else:
        print(f"Loaded {path}")
        return data


# Try with a non-existent file
config = load_config("nonexistent.json")
print(f"Config: {config}")


# ================================================
# Re-raising exceptions
# Catch, log, then send it back up
# ================================================
def critical_operation():
    try:
        risky_code = 1 / 0
    except Exception as e:
        print(f"Logging this error: {e}")
        raise                # re-raise - exception continues up


try:
    critical_operation()
except ZeroDivisionError:
    print("Caught at higher level")