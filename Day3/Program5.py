#Program 5 of Tathastu-Week of Code by shaswat-99
def intersection(l1,l2):
    return list(set(l1)&set(l2))

l1=[str(n) for n in input("Enter List 1: ").split()]
l2=[str(n) for n in input("Enter List 2: ").split()]
print(intersection(l1,l2))
