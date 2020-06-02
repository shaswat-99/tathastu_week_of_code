#Program 6 of Tathastu-Week of Code by shaswat-99   
dicti=[str(dicti) for dicti in input("Enter Words to be added in dictionary separated by space: ").split()]
arr=[str(arr) for arr in input("ENter Characters to be added in Array separated by space: ").split()]
l=[]
for i in dicti:
    if set(i).issubset(set(arr)):
        l.append(i)
print("Possible Words: ",l) 
