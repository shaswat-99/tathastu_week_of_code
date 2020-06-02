#Program 4 of Tathastu-Week of Code by shaswat-99   
n=int(input("Enter the number of items you want to add in a Dictionary: "))
diction={}
for i in range(n):
    key=input("Enter the "+str(i+1)+ " key of Dictionary ")
    value=int(input("Enter the "+str(i+1) + " Values of Dictionary "))
    diction[key]=value
new_dict={}
for key,value in diction.items():
    if value not in new_dict.values():
        new_dict[key]=value
print("Dictionary after removing Duplicate Values: ",new_dict)
