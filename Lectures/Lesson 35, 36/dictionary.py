# Dict = dict({1: 'Data', 2: 'Science', 3: 'Python'})
# my_dict1={}
# my_dict1["Country"]="Korea"
# my_dict1["City"]="Seoul"
# print(my_dict1)
# removedValue=my_dict1.pop("Country")
# print(removedValue)
# print(my_dict1)

my_dict = {'name':'Rose','age':24, 'gender':'Female'}
print(my_dict["name"])
my_dict["name"]="Mary"
print(my_dict["name"])
for key in my_dict:
    print(key)
for values in my_dict.values():
    print(values)
# for key, values in my_dict.items():
#     print(key,values)
# def frequencyCounter(sentence):
#     wordlist=sentence.split()
#     words=dict()
#     for word in wordlist:
#         words[word]=words.get(word,0)+1
#     return words 
# inputSentence=input("Enter a sentence ")
# a=frequencyCounter(inputSentence)
# print(a)