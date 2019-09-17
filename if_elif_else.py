age = input("enter your age")
age= int(age)
 
if 0<age<3:
     print("ticket is free")
elif 3>age>10:
    print("ticket price:10")
elif 10>age>20:
    print("ticket is 30")
else:
    print("ticket is 60")

#in keyword
nmae = "aman"
if 'a' in nmae:
    print("a is present")
else:
    print("not present")
