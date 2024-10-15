import math

# def add_number(number1, number2):
#    return (number1+number2)




# def opposite_array(initial_array):
#     final_array=[]
#     for x in range(len(initial_array)):
#         a=initial_array[-x-1]
#         final_array.append(a)
#     return final_array

def circle_area(radius):
    area_circle=math.pi*radius**2
    return area_circle





def main():
    # first_number=int(input("Please type your first number"))
    # second_number=int(input("Please type your second number"))
    # my_array=[1,2,3,4]
    number=int(input("Please input the radius"))
    area=circle_area(number)
    print(area)

    # sum=add_number(first_number,second_number)
    # print(sum)
    # reverse_array=opposite_array(my_array)
    # print(reverse_array)



if __name__=="__main__":
    main()
    
