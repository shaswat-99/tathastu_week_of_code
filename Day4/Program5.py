#Program 5 of Tathastu-Week of Code by shaswat-99   
names=[str(names) for names in input("enter names of Candidates separated by Space: ").split()]
vote=[]
for i in names:
    vote.append(names.count(i))
dicti={}
for key in names:
    for value in vote:
        dicti[key]=value
        vote.remove(value)
        break
print("Votes Casted: ", dicti)       
l=[]
for i,j in dicti.items():
    x=max(dicti.values())
    if dicti[i]==x:
        l.append(i)     
l.sort()
ans=[]
for keys in l:
    ans.append(keys)
print("The Winner is: ",ans[0])
