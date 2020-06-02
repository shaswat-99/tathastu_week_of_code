#Program 3 of Tathastu-Week of Code by shaswat-99   
n=int(input("Enter the number of items you want to add in a Dictionary: "))
diction={}
for i in range(n):
    key=input("Enter the "+str(i+1) +"key of Dictionary ")
    value=int(input("Enter the "+str(i+1) +"Values of Dictionary "))
    diction[key]=value
val=list(sorted(diction.values()))
print(val[-2])
