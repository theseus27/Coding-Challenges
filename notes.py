#variable.sort() and sorted(variable)
nums = [3, 4, 2, 9 ,4 , 5]
nums.sort() #Requires numpy
nums = sorted(nums)
print(nums)

tups = [("Jimmy", 20), ("Marco", 21), ("Dax", 19)]
tups.sort(key= lambda x: x[0])
print(tups)

#List Comprehension
condition = True
listname = [x for x in range(10) if condition]
tupnames = [(lambda y: y[0]) in tups]   #Don't need "for y"
tupnames = [(y[0]) for y in tups]       #Doesn't work...returns 1
print(tupnames)

#Indexing
word1, word2 = "helloworld", "ello"
print(word1.index(word2) if word2 in word1 else "")
#Reverse word (start, stop, iterator)
word = "hello"
print(word[::-1])

#Rounding
num = 2.308
num = round(num, 1) #OR
num = "%.2f" % num  #OR
print(f'{num:.2f}')

#Empty set notation
numset = set()

#To print stuff on the same line:
print("Hello", end=" ")

#Dictionaries
    #keys, values, items
phonebook = {"Theseus":315, "Boston":617}
[(key,value) for key, value in phonebook.items()]

#Regex
import re
re.split('[^a-zA-Z]', "H3Ll0") #   ^ means not in
