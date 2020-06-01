#Program 1 of Tathastu-Week of Code by shaswat-99        
num=[str(num) for num in input("Enter Elements of Tuple Separated by Space: ").split()]
tup=tuple(num)
ele=input("Enter Element of which you want to count the Occurrence: ")
co=tup.count(ele)
print(f"Occurrence of {ele} is {co} times")
