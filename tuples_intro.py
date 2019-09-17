# tuple data structure
# tuple ca nstroe any data 
#tuple are immutable, once createed cant updated
# no append ,no insert ,no pop, ,no remove 
# tuple are faster 
# def in ()
example = ('aman','kumar','sinha')

# methods in tuple
# count,index
# len function
#slicing
print(example[:2])

# looping in tuple 
# tuple with one element
#tulpe withoiut pasranthesesis
#tuple unpacking
#list inside tuple
# some fn of tuples

mixed = (1,2,3,4,5.0)
 #for loop

for i in mixed:
    print(i)
#note --> whlie loop also can be used

#tulpe with one element
nums = (1)#no tuple
words = ('word1')#errro syntax

print(type(nums))
print(type(words))

num = (1,)#right 
print(type(num))

#tuple unpacking
name = ('aman','kumar','sinha')
fname,manme,lname = (name)
print(fname)

#list insided tuple
fav = ('india',['tokyo','brazil'],'nepal')
fav[1].pop()
print(fav)
fav[1].append('we made it')
print(fav)

# min () max() and sum
print(sum(mixed))
 #new way of tuple samr with list
nums = tuple(range(1,11))
print(nums)

