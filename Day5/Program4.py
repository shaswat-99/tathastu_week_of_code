#Program 4 of Tathastu-Week of Code by shaswat-99
def ks(w,wt,value,size):
    if w==0 or size==0:
        return 0
    if wt[size-1]>w:
        return ks(w,wt,value,size)
    else:
        return max(value[size-1]+ks(w-wt[size-1],wt,value,size-1),ks(w,wt,value,size-1))           
n=int(input("Enter total number of items: "))
value=[]
wt=[]
for i in range(n):
    val=int(input("Enter value of "+ str(i+1)+" item: "))
    value.append(val)
    wgt=int(input("Enter weight of "+ str(i+1)+" item: "))
    wt.append(wgt)
w=int(input("Enter Weight Capacity"))  
size=len(value)
print(ks(w,wt,value,size))
