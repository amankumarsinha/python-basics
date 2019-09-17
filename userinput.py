#input funtion is used
name = input("enter you name")
print("your name "+name)
# input is ALWAYS a string
age = input("enter your age")
print("your age "+age)
# to convert input in interger int() fuction is used
age =int( input("enter your age"))
print("your age "+str(age))
#str() to string     float() to float

#more than one varialbe in single line in single line
nam,year = "aman" , 24
print("hello" + nam + "your age" +str(year))


#more inputs in single line
naam,years = input("enter your name and age ").split()  # we can use , to seprate output like split(",")
print(naam)
print(years)
col,std = input("enter your name and age ").split(",")
print(col)
print(std)

