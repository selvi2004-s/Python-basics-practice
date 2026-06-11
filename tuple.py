# fast list can NOT be modified, immutable cant change elements 
#"frozen list", has indexing but you can't change an element inside 

# Create a tuple
t = (1, 2, 3, 4)
print(t)


#Access elements 
print(f'First element: {t[0]}')
print(f'Slice: {t[0:2]}')
print(f'Bool: {3 in t}')


#Assignment 
(x,y,z,)= range(1,4)
print(x)
print(y)
print(z)

