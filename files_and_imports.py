# ================================================
# FILE I/O, JSON, IMPORTS — PRACTICE
# Save this as files_and_imports_practice.py
# ================================================
import json
import os


# ================================================
# Writing a text file
# "w" mode = overwrite (or create if doesn't exist)
# ================================================
with open("notes.txt", "w") as f:
    f.write("Hello, file!\n")          # \n = newline
    f.write("This is line two.\n")
    f.write("And line three.\n")

print("File written.")


# ================================================
# Reading - method 1: all at once
# ================================================
with open("notes.txt", "r") as f:
    content = f.read()                 # entire file as one string
    print("Full content:")
    print(content)


# ================================================
# Reading - method 2: list of lines
# Each line keeps its \n at the end
# ================================================
with open("notes.txt", "r") as f:
    lines = f.readlines()              # list of strings
    print(f"Got {len(lines)} lines")
    print(lines)                       # see the \n attached to each


# ================================================
# Reading - method 3: line by line (best for big files)
# Uses much less memory - reads as it goes
# ================================================
with open("notes.txt", "r") as f:
    for line in f:
        print(f"Line: {line.strip()}")  # strip() removes the \n


# ================================================
# Appending to a file
# "a" mode = add to end, don't overwrite
# ================================================
with open("notes.txt", "a") as f:
    f.write("Appended line!\n")

# Verify by reading again
with open("notes.txt", "r") as f:
    print("After appending:")
    print(f.read())


# ================================================
# writelines() - write a list of strings at once
# Note: it does NOT add newlines automatically
# ================================================
poems = ["Roses are red\n", "Violets are blue\n", "Python is fun\n"]
with open("poem.txt", "w") as f:
    f.writelines(poems)

print("Poem written.")


# ================================================
# Binary files
# Use "rb" / "wb" instead of "r" / "w"
# Returns bytes objects, not strings
# ================================================
# Write some bytes
data = b"This is bytes data \x00\x01\x02"   # the b"" makes it bytes
with open("binary.dat", "wb") as f:
    f.write(data)

# Read them back
with open("binary.dat", "rb") as f:
    raw = f.read()
    print(f"Binary content: {raw}")
    print(f"Type: {type(raw)}")        # <class 'bytes'>

# Practical: copy a file using binary mode
with open("notes.txt", "rb") as src:
    contents = src.read()
with open("notes_copy.txt", "wb") as dst:
    dst.write(contents)
print("File copied via binary mode.")


# ================================================
# JSON - converting Python <-> JSON string
# ================================================
person = {
    "name": "Selvi",
    "age": 22,
    "skills": ["Python", "Java"],
    "active": True,
    "salary": None              # → null in JSON
}

# Python dict -> JSON string
json_string = json.dumps(person)
print(f"As JSON string: {json_string}")

# JSON string -> Python dict
back_to_dict = json.loads(json_string)
print(f"Back to dict: {back_to_dict}")
print(f"Name: {back_to_dict['name']}")


# ================================================
# JSON - pretty printing
# indent=4 makes it readable
# ================================================
pretty = json.dumps(person, indent=4, sort_keys=True)
print("Pretty JSON:")
print(pretty)


# ================================================
# JSON - writing to a file (dump, no 's')
# ================================================
with open("person.json", "w") as f:
    json.dump(person, f, indent=4)
print("JSON saved to person.json")


# ================================================
# JSON - reading from a file (load, no 's')
# ================================================
with open("person.json", "r") as f:
    loaded = json.load(f)
print(f"Loaded from file: {loaded}")


# ================================================
# Realistic example: read JSON, modify, write back
# ================================================
with open("person.json", "r") as f:
    data = json.load(f)

data["skills"].append("Django")        # modify
data["age"] += 1                       # birthday!

with open("person.json", "w") as f:
    json.dump(data, f, indent=4)

print(f"After update: {data}")


# ================================================
# Imports - using the helpers.py module
# (Create helpers.py in the same folder - see below!)
# ================================================
# Style 1: import the whole module
import helpers
print(helpers.greet("Selvi"))
print(f"PI from helpers: {helpers.PI}")

# Style 2: import specific names
from helpers import multiply, PI
print(multiply(3, 4))
print(f"PI directly: {PI}")

# Style 3: aliasing
import helpers as h
print(h.greet("Aram"))


# ================================================
# The __name__ trick
# This block only runs if you run THIS file directly
# Not when it's imported from somewhere else
# ================================================
print(f"My __name__ is: {__name__}")    # always prints when this file runs

if __name__ == "__main__":
    print("Running directly - this is the main script!")
    # Put your "test" code or "main entry point" here
else:
    print("I was imported, not run directly")


# ================================================
# Cleanup - delete the test files we created
# (Uncomment to clean up after running)
# ================================================
# os.remove("notes.txt")
# os.remove("notes_copy.txt")
# os.remove("poem.txt")
# os.remove("binary.dat")
# os.remove("person.json")
# print("Cleanup done.")