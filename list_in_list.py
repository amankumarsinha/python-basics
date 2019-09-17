matrix  = [[1,2,3],[1,4,7],[1]]
print(matrix[0])
for i in matrix:
    print(i)

# to show elements of sublist 
for sub in matrix:
    for i in sub:
        print(i)
        
#fetching elements of sublist
print(matrix[1][2])

#type fun used to find type of data
print(type(matrix))