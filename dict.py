# Dictionary key value pairs
# Indexed by keys

d = {"pet": "dog", "age": 5, "name": "spot"}
print(d)
d = dict(pet="dog", age=5, name="spot")
print(d)


#Get keys and values 
print(f'Items: {d.items()}')
print(f'Keys: {d.keys()}')
print(f'Values: {d.values()}')

#Getting value from key 
print(f'Name: {d["name"]}') #should use " " , will throw an error if the key is not found

#Add an item 
d['trick']='sit' #key equals value 
#if key already exists it changes its value, key itself cant change we can just delete the key or change the value not key 

#Removing item 
del d['trick']
print(f'Items: {d.items()}')

#Removing item Testing for existence
if 'name' in d:
    print(d['name'])

#Looping 
for key in d.keys():
    print(f'Loop: {key}={d[key]}')