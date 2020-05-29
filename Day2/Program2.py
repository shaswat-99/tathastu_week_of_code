#Program 2 of Tathastu-Week of Code by shaswat-99
def feb(n):
    if n<=1:
        return n
    else:
        return (feb(n-1)+feb(n-2))

n=int(input("Enter number of terms "))
if n<=0:
    print("Input Positive Number")
else:
    print("Febonacci Series")
    for i in range(n):
        print(feb(i))  
