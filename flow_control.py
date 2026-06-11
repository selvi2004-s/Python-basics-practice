# IF ELSE ELIF
x = False
if x:  # means if true
    print("yes")
    print("again")
else:
    print("no")

# Condition evaluation
x = 100
y = 25

# IF ELSE
print("start")
if y == x:
    print("equal to")
if y != x:
    print("not equal")
if y < x:
    print("less then")
if y > x:
    print("greater then")
if y <= x:
    print("less then or equal then")
if y >= x:
    print("more then or equal then")

# ELIF
# Elif is the switch solution (to not run all ifs stop if found true)
x = 25
print("Elif is the switch solution")
if x == 25:
    print("x=25")
elif x == 70:
    print("x=70")
elif x == 27:
    print("x=70")
else:
    print("none was true")

# Nested statements

x = 82
if x > 50:
    print("over 50")
    if x > 60:
        print("over 60")
        if x > 70:
            print("over 70")


# While loops

x = 0
while x < 10:
    x += 1
    print(f"x={x}")
print("Done")

# Pass
# x = 5
# while x < 10:
# pass

# print ('Test2 is done') # will not print its an infinite loop


# Continue
x = 0
while True:  # Loop forever
    x += 1
    if x < 5:
        print(f"x<5 {x}")
        continue
    print(f"Do sth {x}")

    if x == 10:
        print(f"Exiting x={x}")
        break

print("Complete!")


#For loop

l = [1, 2, 3, 4]  # List
t = (1, 2, 3, 4)  # Tuple
s = {1, 2, 3, 4}  # Set
for i in l:  # dont need to increment it does for us
    print(f"i={i}")


#For loop for dictionaries 
x = dict(Bryan=46,Selvi=22,Vika=10)
print(x)

for k in x.keys():
    print(f'Keys: {k}={x[k]}')

for k,v in x.items():
    print(f'{k}={v}')

#Range 
x=range(5)
print(x)
for i in x:
    print(f'Range: {i}')


#Range start, stop and step 
x=range(5,20,3)
print(x)
for i in x:
    print(f'Stepped: {i}')

