#Sets {}
#Unorder, unqiue (cant have the same things), 
#immuatable data type (once we add cant change individual items only can add and remove)
#in hash table 


#FAST LOOKUP

#Creating set 
s = {1,2,2,2,3,4,5} #python automatically removes duplicates
print(s)

l=['Selvi', 8, True]
s = set(l)
print(s)

#Adding
print(s)
s.add('Hello')
print(s)
s.update([5,'Bye','Selvi'])
print(s)
print(s)


#Remving 
s.discard('Hello') #will not give error 
s.remove('Selvi')  #will give error 
v=s.pop() #removes random element and gives the value 

#Cant change items 
print ('Bye' in s) #can just see whether an item is in the set or not 

#to append set elements can use intersection (only elements that are in both), union (combines all elements),
# difference (returns elements that are in x but not in y ), symmetric difference(returns the elements that are in x or y but not both ) methods 