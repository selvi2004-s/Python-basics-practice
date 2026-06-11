# Strings also start indexing with 0

# Making strings

first = "Selvi"
last = "Hambardzumyan"


print(first + " " + last)

print(f"Hello my name is {first} {last}")  # formatting

# hack
hers = "Selvi's"
print(hers)

# String is unicode sequence of characters
s1 = chr(72)  # H
s2 = chr(105)  # i
print(s1 + s2)

# Escape characters
print(f"Hello\nWorld")  # \n new line

name = "Selvi"
age = 22
print(f"My name is {name} I am {age}")

# Basic String Operations

str = "Selvi , Selv"

print(len(str))  # length
print(str * 3)
print(str + str)

print(str.replace("Sel", "El"))  #replaces
print(str.split(","))  #creates new data type
print(str.startswith("s"))
print(str.upper())
print(str.lower())


# Slicing | Getting a sub string
print(str[0:4])
print(str[0:])
print(str[1:])
print(str[-1])  # negative indexing

# Getting index
l = "K"  # Returns -1 when str doesnt contain that character
print(str.find(l))

i = ","
print(str.index(i))  # throws error if character doesnt exist

x = str[0:3]
print(x)
