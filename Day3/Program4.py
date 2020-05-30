#Program 4 of Tathastu-Week of Code by shaswat-99
l=[str(n) for n in input("Enter all the elements of List: ").split()]
dup=[]
for i in l:
    if i not in dup:
        dup.append(i)
print(f"The New List is {dup}")   
