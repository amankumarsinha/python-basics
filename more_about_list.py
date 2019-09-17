#generate list with range fun
#something about pop()
#index method 
# pass list to afunction

n = list(range(1,11))
print(n)

print(n.pop())# returns the deleted item
 
print(n.index(5))# return the position of the given number fist occurance
print(n.index(5,3))# you can assing from where to search
print(n.index(5,2,6))# you can stop at particular position

# passing list ot function
def neg(l):
    nega = []
    for i in l:
        nega.append(-i)
    return nega

print(neg(n))
 
