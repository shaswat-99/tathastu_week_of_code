#Program 2 of Tathastu-Week of Code by shaswat-99       
n=int(input("Enter number of tuples you want to create: "))
i=0
l1=[]
while i<n:
    l=[str(l) for l in input("enter elements of tuple separated by space: ").split()]
    i+=1
    l1.append(tuple(l))  
print("The Original Tuple List is: ",l1) 
index=int(input("Enter Index according to which sort is performed: "))
l1.sort(key=lambda x: x[index])
print(f"Tuple List after sorting is: {l1}")   
