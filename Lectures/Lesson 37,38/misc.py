# #1.zip function
# my_tuple=(1,2,3)
# my_list=["hello","my","name"]
# my_zip=zip(my_tuple,my_list)
# print(list(my_zip))

# #2.filter function
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def is_even(number):
#     return number%2==0
# filterednumbers=list(filter(is_even, numbers))
# print(filterednumbers)

# #3.lambda function
# is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
# for item in is_even_list:
#     print(item())
# x=lambda a:a+10
# print(x(5))
# y=lambda c:(c%2 and "Odd" or "Even")
# print(y(5))

# #3.1lambda with conditionals
# max=lambda a,b :a if(a>b) else b
# print(max(2,3))

# #3.2lambda with filter
# programming_languages = ["C", "C++", "Java", "Python", "JavaScript", "Ruby", "Swift"]
# javalang=list(filter(lambda lang: "Java" in lang, programming_languages))
# #4map
# squarednumbers=map(lambda arg: arg**2, numbers)
# print(list(squarednumbers))
def addNum(number1):
    sum=number1+1
    return sum
sum_list=[3,4,5,6,1,7]
sum1=list(map(addNum, sum_list))
print(sum1)