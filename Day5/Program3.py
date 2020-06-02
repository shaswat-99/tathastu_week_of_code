#Program 3 of Tathastu-Week of Code by shaswat-99   
def stolen(house):
    if len(house)==0:
        return 0
    if len(house)==1:
        return house[0]
    if len(house)==2:
        return max(house[0],house[1])
    nth=[0]*len(house)
    nth[0]=house[0]
    nth[1]=max(house[0],house[1])
    for i in range(2,len(house)):
        nth[i]=max(nth[i-1],nth[i-2]+house[i])
    return nth[-1]            

house=[int(house) for house in input("Enter values of every House in a Sequence:  ").split()]
print("Maximum Value Stolen is: ",stolen(house))
