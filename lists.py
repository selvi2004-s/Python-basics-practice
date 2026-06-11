# Lists []

# Doesnt have to be the same data type, index starts from 0

# Creating
x = ["Selvi", "Someone", 47, "Hey"]
print(x)
print(len(x))  # length

print(f"Slice: {x[1:3]}")
print(f"Zero: {x[0]}")

# Adding items | Append, insert

# Append
x.append(7)
x.append("cats")
print(x)

# Insert
x.insert(0, "Hey")  # doesnt remove just inserts and shifts others to the right
print(x)


# Removing items #remove, pop, delete

# remove just removed the element and returns none
x.remove("Hey")
print(x)

# pop removed and returns the element of list
i = x.index("Selvi")
print(f"Food: {x.pop(i)}")
print(f"List: {x}")

i = x.index(47)
del x[i]  # will delete a specifix index and return nothing


# Extending - adds elements from another list
y = ["Cats", "Dogs", "Birds"]
x.extend(y)
print(f"List: {x}")


# Sorting (ascending and descending) BUT LIST HAS TO HAVE THE SAME TYPE
x.remove(7)  # removing 7 so that every item is string
print(f"List: {x}")
x.sort()  # sorts alphabetical
print(f"Sort: {x}")
x.reverse()  # sorts reverse of alphabetical
print(f"Sort: {x}")

# Copy
y = x.copy()  # Makes a new list and copies items of x to the new list
y.reverse()
y.append("Apples")
print(f"Original: {x}")
print(f"New: {y}")

# Deleting
del y  # deletes the whole list
x.clear()  # keeps the list but deletes all the elements
print(f"Clear: {x}")
print(len(x))

# List can contain other list (equal to like array of arrays)
x = []
y = [1,2,3]
z=['Bryan','Cairns']
x.append(y) #list in list 
x.insert(0,z)

print(f"Merged: {x}") #list in list , our list is made up of all 2 smaller lists 
print(len(x))
print(f'0: {x[0]}')
print(f'0: {x[0][0]}') #gives the first item of first list inside of the list 



# Changing one item 
x = [1,2,3,4]
x[0]='Hey'
print(x)