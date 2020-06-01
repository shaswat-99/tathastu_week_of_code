#Program 6 of Tathastu-Week of Code by shaswat-99        
from itertools import combinations
ans=[]
subs=[]
def sub_list(l):
    for i in range(0,n+1):
        temp=[list(x) for x in combinations(l,i)]
        if len(temp)>0:
            subs.extend(temp)
    return subs
def sum_sub(subs):
    for ele in subs:
        Sum=(sum(ele))
        ans.append(Sum)
    return ans

l=[int(num) for num in input("Enter elements of list separated by Space: ").split()]
n=len(l)
item=1
sub_list(l)
sum_sub(subs) 
while True:
    if item not in sum_sub(subs):
        print(f"The least integer which is not in list and not represented by Summation of sub elements is: {item}")
        break    
    item+=1
