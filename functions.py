# function defining in python 
#synatax def(keyword) fn_name (argument): 
#                     return a+b
                                         
def add(a,b):# inputs can be aby variabe int string float
    return a+b
total  = add(5,8)
print(total)
print(add(2,8))
# another wy to show output

def ads(a,b): #return can be negleted if you want
    print(a+b)
ads(5,6)
  
def even_odd(n):
    if n%2 == 0:
        return "even"
    else:
        return "odd"# else can be removed 

print(even_odd(4))

# more reduced function
def even(m):
    return m%2==0 # true if even 

print(even(5))

def great(a,b):
    if a>b:
        return a
    return b

print(great(10,7))

#gretest of three number
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

print(greatest(4,45,9))


# funtion inside a funtion 
# funtion to find greatestt of two,thee no.

def new_great(a,b,c):
    big=great(a,b)
    return great(big,c)

print(new_great(10,4,5))


def fib(n):
    a = 0
    b = 1
    if n==1:
        print(a)
    elif n==2:
        print(a,b ,end = " ")
    else:
        print(a,b ,end = " ")
        for i in range (n-2):
            s = a + b
            a = b
            b = s
            print(s , end = " ")

fib(8)

# function can eturn two values
def mul1(int1,int2):
    add = int1+int2
    mul = int1*int2 
    return add,mul # it returns tw ovalues but as tupel


print(mul1(3,4))

add1 ,mul2 =mul1(4,5)
print(add1,mul2)


#max and min fn

n = [4,56,89,9]

print(min(n))
print(max(n))

import numpy as np
a = np.array(10,19,19)
print(a)
