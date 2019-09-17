fruits = ['apple','banaba','orage','mango']
if 'teen'in fruits:
    print('preseent')
else:
    print('not present')

#methods in list

print(fruits.count('apple'))

#sorting
fruits.sort()
print(fruits)

# if you want to just print the sorted list but not sor the list
number = [3,5,73,1,9]
print(sorted(number))# sorted
print(number)#original

#clear
#number.clear()
#print(number)

#coping a list
no_copy = number.copy()
print(no_copy)