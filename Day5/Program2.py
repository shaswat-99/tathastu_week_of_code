#Program 2 of Tathastu-Week of Code by shaswat-99   
def replace(l):
    for i in range(n-1):
        l[i]=max(l[i+1:])
    return l
l=[int(l) for l in input("Enter elements of Array separated by Space: ").split()]
n=len(l)
print("Array After Replacing each element by max right is: ",replace(l))
