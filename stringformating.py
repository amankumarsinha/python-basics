name = "aman"
age = 45
print("hello" + name + "your age " + str(age)) # long syntax 
 #python 3 improve syntax  
print("hello {} your age {}".format(name,age))
#  this is not working dint know why

#python 3.6 more improve
print(f"hello {name}your age {age}")

lang = "aman kumar sinha"
#string slicing 
# syntax --->[start:stop-1:step] step skip no of char
print(lang[2:4]) #2 to 3 char
print(lang[1:-1:2])
print(lang[::-1]) #count backworks