#Program 3 of Tathastu-Week of Code by shaswat-99
n = int(input("Enter the value of N: "))
for i in range(n):
    print(" " * i + "*" + "  " * (n-i-1) + "*")
for i in range(n):
    print(" " * (n-i-1) + "*" + "  " * i + "*")  
