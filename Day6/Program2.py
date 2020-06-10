#Program 2 of Tathastu-Week of Code by shaswat-99 
l=[]
l1,l2,l3=[],[],[]
def sort(l):
    for i in l:
        if i==0:
            l1.append(i)
        if i==1:
            l2.append(i)
    l3=l1+l2 
    print(l3)             
n=int(input("Enter total numbers of 0's and 1's you want to input "))
for i in range(n):
    i1=int(input("Enter "+str(i+1)+"st 0 or 1=> "))
    l.append(i1)
sort(l)
