# import math
# a = 4
# b = "Hello"
# c = False
# def say_hello(name, message): 
#     print(name, message)
    
# say_hello(name="Mark", message="Hello")

# def calculate_average(number1, number2):
#     print((number1+number2)/2)
# calculate_average(2,3)

# def calculate_areaofcircle(radius):
#     area= math.pi*radius**2
#     return area
# my_area = calculate_areaofcircle(5)
# print(my_area)

# def calculate_areaoftriangle(side, height):
#     area = (side*height)/2
#     print(area) 
# # calculate_areaoftriangle(4,5)

# # ----- Conditionals ----
# number1= 5
# number2=5
# if number1<number2 :
#     print(str(number1)+"<"+ str(number2))

# elif number1==number2 :
#     print("They are equal")

# else: 
#     print("error")

# WAGE = 10

# def calculate_wage(workinghour):

# #     if workinghour<=40:
# #         weekly_wage=WAGE*workinghour
    
# #     else: 
# #         weekly_wage=WAGE*40+(workinghour-40)*15
# #     print(weekly_wage)

# # calculate_wage(60)

# def hire_manager(gpa, age, interview_score, aptitude_score):
#     total_points=0
#     if gpa>3.3 and age>24:
#         total_points+=1
#     if 6<interview_score<9:
#         total_points+=1
#     elif 9<=interview_score<=10:
#         total_points+=2
#     if aptitude_score>85:
#         total_points+=1
#     if total_points<=2:
#         print("not hired")
#     elif total_points==3:
#         print("hired as a Junior Salesperson")
#     else :
#         print("Hired as a Manager-In-Training")

# hire_manager(4, 9, 90)

def calculate_fraction(number1,number2):
    try:
        fraction= number1/number2
    except ZeroDivisionError: #divided by zero
        print("Error occured")
    else: 
        print(fraction)
calculate_fraction(2,0)

   
# ---------------------------- Exercise 2: The modern Architect ----------------------------
# TODO: Complete the implementation of calculate_frustum_volume() and calculate_ac_units().

# Function to calculate the volume of a frustum
def calculate_frustum_volume():
    # Your code here
    ...

# Function to calculate the number of AC units needed
def calculate_ac_units():
    # Your code here
    ...

# ---------------------------- Exercise 3: The Solar Panel Problem ----------------------------
# TODO: Complete the implementation of calculate_triangle_area() and calculate_energy().

# Function to calculate the area of a triangle
def calculate_triangle_area():
    # Your code here
    ...

# Function to calculate the energy generated by the solar panels
def calculate_energy():
    # Your code here
    ...










