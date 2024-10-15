# my_array=[]
# for x in range(5):
#     a = input("Please input a number: ")
#     my_array.append(a)
        
# print(my_array)

# def sort_array(array1,array2):
#     for x in range(len(array1)):
#         for y in range(len(array2)):
#             print(array1)
#             if array1[x]>array2[-y]:
#                 b= array2[-y]
               
#                 array1[x]=b
#         array2=array2[0:len(array2)-1]

#     return array1

def sort_array(array):
    for x in range(len(array)):
        sub_array = array[x:len(array)]
        print("---------------------------------------")
        print(array)
        print(sub_array)
        print("---------------------------------------")
        for y in range(len(sub_array)):
            if(x==1 and y==1):
                print(array)
            if (array[x] > sub_array[y] and x+1<=len(array)):
                a=array[x]
                b=sub_array[y]
                array[x]=b
                array[x+1]=a


my_array=[5,4,3,2,1]
resultarray=sort_array(my_array)
print(resultarray)