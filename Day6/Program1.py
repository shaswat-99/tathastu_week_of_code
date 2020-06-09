#Program 1 of Tathastu-Week of Code by shaswat-99 
string=input("Enter a string: ")
l=list(string)
c=[]
for i in l:
    c.append(l.count(i))    
dicti={}
for key in l:
    for value in c:
        dicti[key]=value
        c.remove(value)
        break
l1=dicti.values()
l2=[]
for i in l1:
    if i%2==0:
        continue
    elif i%2!=0:
        l2.append(i)
l3=[]
for i in l2:
    if i==max(l2):
        continue
    else:
        l3.append(i)

l4=l2

if not l2:
    print("After rearrangement, Palendrome string will be formed")    
elif not l3:
    print("The Palendrome will be formed after removing ",len(l4)-1," characters")     
else:
    remove=len(l3)
    print("The Palendrome string will be formed after removing ",remove," characters") 
