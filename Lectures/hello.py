# Asking the size of the table
# side= int(input("How big is your table?"))
# Printing the size of the table
# (print(side))
# Printing the area of the table
# print("The area of the table is " + str((side**2)-(side/2)*(side/2)/2))
# import math
# radius = int(input("What is the radius of the circle"))
import math
# print(radius)
# print("the area of the circle is", "{:.2f}".format((math.pi*radius**2)))
def my_function(side_a=2,side_b=3):

    side_c= (side_a**2+side_b**2)**0.5
    return(side_c, side_a, side_b)
result, result2, result3 = my_function()
print(result2)

