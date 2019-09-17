#defining list
number = [1,2,3,4,5]
print(number)

word = ['aman','kumar','sinha']
print(word)

mixed = [1,"aman",2,'kumar']
print(mixed)
# replacing and adding new in list with different cases
mixed[1] = "sinha"
print(mixed)
mixed[1:3] = [23,67]
print(mixed)
mixed[1:] = "aman"
print(mixed)
mixed[1:] = ["aman","kumar"]
print(mixed)
mixed[1:3] = ["aman","kumar"]
print(mixed)

#adding items in list
fruits = ['apple','orange']
fruits.append('mango')# add items at last
print(fruits)
# to add item at any possition   insert method is used
fruits.insert(1,"papaya")
print(fruits)
veg = ["gobi","onion"]
#concatination of two string
edible = fruits+veg
print(edible)

# to add another string in 1 string 3xtend method is used 
fruits.extend(veg)
print(fruits)

#list inside a list 
fruits.append(veg)
print(fruits)

#delete from list
#pop method delete last items from list by default
fruits.pop()
print(fruits)
fruits.pop(3)
print(fruits)
#delete oprator
del fruits[1]
print(fruits)
#remove method
fruits.remove('apple')
print(fruits)

