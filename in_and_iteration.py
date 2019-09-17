userinfo = {
     'name': 'aman',
     'age': 34,
     'fav': ['3 ididot','lig','ololo']  # key can be string or int
 }
 # to check if key exist in dictionary
if 'name' in userinfo:
     print('present')
else:
    print('not present')

# check if values exist in dict
if 'aman' in userinfo.values():# important for values
    print('present')
else:
    print('not present')

#loop in dict
for i in userinfo:
    print(i)

#for values 
for i in userinfo.values():
    print(i)

values = userinfo.values()
print(values)

key = userinfo.keys()
print(userinfo)

#print values using keys
for i in userinfo:
    print(userinfo[i])

#itemss method
items = userinfo.items()
print(items)
print(type(items)) # it return key paies in tuples

for key, values in userinfo.items():
    print(f"key is {key} and values is {values}")