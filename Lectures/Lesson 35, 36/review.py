import middle
def maxValue(givenlist):
    b=0
    for x in range(len(givenlist)-1):
        if givenlist[x]>givenlist[x+1]:
            b=givenlist[x]
        elif givenlist[x]<givenlist[x+1]:
            b=givenlist[x+1]  
        else:
            b=b
    return b






def main():
    my_list=[1,2,3,4,5]
    a=int(maxValue(my_list))
    m1=middle.Middle("Mark",[14,27,19,33,56])
    m1m=m1.getMiddleNumber()
    print(a+m1m)


if __name__=="__main__":
    main()