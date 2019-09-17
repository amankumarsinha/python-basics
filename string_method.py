name = "aman kumar sinha"
# len function
length = len(name)
print(length) 
 #give string length
print(len("aman"))

#lower method
print(name.lower()) #.is used in methods

#upper() method
print(name.upper())

#title() method
print(name.title())

#count() method 
print(name.count("a"))

# strip  method remove spacess
names = "  aman   "
dots ="......."
#lstrip() method ---> remove left spaces
print(names + dots)
print(names.lstrip()+ dots)
#rstrip() method ----> remove right spaces
print(names + dots)
print(names.rstrip()+ dots)
# strip() ---> remove both side spaces
print(names + dots)
print(names.strip()+ dots)
print(name.strip().lower().count("a")) # no of methos 

#replace and find methods
string = "he is a good boy and is good player"
print(string.replace("is","was")) #we can use to change __(space ) with anything
#to replace at particular no of is
print(string.replace("is","was",1))
  
#to find a word position
print(string.find("is",1)) #to get  searching from 1 is position

#center method add * to string
naam = "aman"
print(naam.center(11,"*"))