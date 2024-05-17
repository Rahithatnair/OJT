
# Iterate over keys and values in a dictionary.

dictionary={'name':"Raahitha",'age':22,'place':"venjaramoodu"}
for key, value in  dictionary.items():
    print(key, value)
    
 # Create a dictionary and access its elements
dict = {'name': 'raahi', 'age': 22, 'city': 'tvm'}
print("Name:", dict['name'])
print("Age:", dict['age'])
print("City:", dict['city'])

# Add a key-value pair to an existing dictionary.
updict = {'name': 'raahi', 'age': 22}
updict['city'] = 'tvm'
print("Updated dictionary:", updict)

# Check if a key exists in a dictionary
diction = {'name': 'raahi', 'age': 22, 'city': 'tvm'}
key_to_check = 'city'
if key_to_check in diction:
    print(f"{key_to_check} exists in the dictionary.")
else:
    print(f"{key_to_check} does not exist in the dictionary.")

