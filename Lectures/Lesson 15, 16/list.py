

# def smallest_number(initial_array):
#     min=initial_array[0]
#     for x in range(len(initial_array)):
#         if min>initial_array[x]:
#             min=initial_array[x]
#     return min


def count_vowels(word):
    vowels='aeiou'
    my_array=[]
    for letter in word.lower():
        if letter not in vowels:
            my_array.append(letter)
    return my_array



def main():
    # array1=[5,7,23,44,1,12,8,99]
    # minimum=smallest_number(array1)
    # print(minimum)
    word="Hello"
    print("The vowels in " + word+ " are " + str(count_vowels(word)))


if __name__=="__main__":
    main()