#Program 4 of Tathastu-Week of Code by shaswat-99
cp=float(input("Enter Cost Price of the Product "))
sp=float(input("Enter Selling Price of the Product "))
profit=sp-cp
print(f"Profit= {profit}")
new_sp=1.05*profit+cp
print(f" Selling Price after 5% extra profit on product = {new_sp}")
