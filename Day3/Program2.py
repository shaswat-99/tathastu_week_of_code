#Program 2 of Tathastu-Week of Code by shaswat-99
result=[]
def perm_n(l,i,size):
    if i==size:
        result.append(''.join(l))
    else:
        for j in range(i,size):
            l[i],l[j]=l[j],l[i]
            perm_n(l,i+1,size)
            l[i],l[j]=l[j],l[i]          
str_i=input("Enter a string")
perm_n(list(str_i),0,len(str_i))
print("Resulting Permutation= ",str(result))
