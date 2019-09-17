#to  represent real life data
#collection of data in key : value pair

user = {'name' : 'aman','age' : 20}
print(user)
print(type(user))

# 2 method 
user1 = dict(name = 'aman',age = 20)
print(user1)
print(user1['name'])

# type of data store in dict
#---> number ,string, list,dict

userinfo = {
     'name': 'aman',
     'age': 34,
     'fav': ['3 ididot','lig','ololo']
 }
print(userinfo['fav'])


#dict inside a dict
userama = {
    userinfo = {
     'name': 'aman',
     'age': 34,
     'fav': ['3 ididot','lig','ololo']
 }

}

# how to add data in dict
useraman ={}
useraman['name'] = 'aman'
print(useraman)