#Program 5 of Tathastu-Week of Code by shaswat-99   
def is_even(l):
    l_even=[]
    for i in l:
        if i%2==0:
            l_even.append(i)
    l_even.sort() 
    return l_even
def is_odd(l):
    l_odd=[]
    for j in l:
        if j%2!=0:
            l_odd.append(j)
    l_odd.sort(reverse=True)
    return l_odd


l=[int(l) for l in input("Enter list of integers separated by Space: ").split()]
print("Ascending Order of Even Elements of list: ",is_even(l))
print("Descending Order of Odd Elements of List: ",is_odd(l))
