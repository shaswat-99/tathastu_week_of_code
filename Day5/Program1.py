#Program 1 of Tathastu-Week of Code by shaswat-99   
def replace(num):
    val=str(num).replace("0","5")
    return int(val)
num=int(input("Enter a Integer: "))
print(f"Integer after replacing \"0\" with \"5\" is : {replace(num)}") 
