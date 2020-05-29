#Program 1 of Tathastu-Week of Code by shaswat-99
def even_odd(n):
    if n%2==0:
        return True
    else:
        return False

def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
                break
        else:
            return True
    else:
        print("Invalid Input")

def pal(n):
    temp=n
    rev=0
    while n>0:
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if temp==rev:
        return True
    else:
        return False

def arms(n):
    sum=0
    temp=n
    while temp>0:
        dig=temp%10
        sum=sum+dig**3
        temp=temp//10
    if n==sum:
        return True
    else:
        return False

def val():
    n=int(input("Enter a Number "))
    if even_odd(n):
        print("Even Number")
    else:
        print("Odd Number")
    if prime(n):
        print("Prime Number")
    else:
        print("Not Prime Number")            
    if pal(n):
        print("Palindrome Number")
    else:
        print("Not Palindrome Number")    
    if arms(n):
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")    
val()   
