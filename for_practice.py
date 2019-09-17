#ask user to enter name and count each character
name = input("enter your name ")
temp = ""
for i in range(len(name)):  #bydefault it strt from zero bno neccary to give start
    if name[i] not in temp:
        print(f"{name[i]}:{name.count(name[i])}")
        temp += name[i]