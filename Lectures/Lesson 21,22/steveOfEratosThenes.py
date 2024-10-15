import math
while True :
    def start():
        x= input("Please input the maximum number")
        if x==-1:
            break
        else:
            x
min_number=2
worksheet=[None,None]+list(range(min_number,max_number+1))

def sieve(current_value,max_value):
    for i in range (int(math.sqrt(max_value+1))):
        for i in range (current_value*current_value,max_value+1,current_value):
            worksheet[i]=None
        current_value=+current_value+1
    return worksheet

def remove_none (initialList):
    modifiedList=[]
    for i in range (len(initialList)):
        if initialList[i] is not None:
            modifiedList.append(initialList[i])
    return modifiedList


max_number=start()
newlist=sieve(min_number,max_number)
finalList=remove_none(newlist)
print(finalList)