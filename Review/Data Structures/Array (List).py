#ARRAYS
    #Python uses lists, no built in array type
    #All same data type
    #Good for accessing and insertion/removal at the end    O(1)
    #Searching a sorted array                               O(log n)
    #General searching/insertion/removal                    O(n)

    ##Insert/Pop throws index error if pop/insert from empty list or index does not exist
    #Index/Remove throws ValueError if value is not in list
    
    
#List comprehension
#Long way
squares = []
for x in range(10):
    squares.append(x**2)
#Short way
even_squares = [x**2 for x in range(10) if x%2 == 0]
print(even_squares)

#Dynamic Array
my_array = [1, 1, 1, 1, 2, 2, 2, 2, 3, 4]

#Editing
my_array.append(1)      #Appends value to the end
my_array.insert(1, 5)   #Add element at that index (index, value)
my_array.remove(5)      #Removes first element w/ value
my_array.pop(0)         #Removes element at position (default last)

my_array.sort()         #Sorts array
my_array.reverse()      #Reverses order of array
my_array.clear()        #Removes all elements in array
my_array.extend([1])    #Adds elements of list or other iterable to end of array

#Data retrieval
my_array.count(2)       #Returns # of elements w/ value
my_array.index(1)       #Returns index of first element w/ value
my_array.copy()         #Returns a copy of array

print(len(my_array))    #Get length of array

#Arrays w/ NumPy
    #Is more for array manipulation that insertion and stuff
import numpy as np
np_array = np.array([1], int)
print(np_array)

my_matrix = np.array([["name", "age", "major"], ["theseus", "20", "CS"], ["marco", 21, "CS"], ["dax", 19, "soc"]])

#Print row (element in matrix)
print(my_matrix[0])

#Print column (something in each position)
names = [];
for row in my_matrix:
    names.append(row[0])
print(names)

np_matrix = np.asarray(my_matrix)
print(np_matrix.transpose())    #Flips rows and columns


nums = np.arange(10)
print(nums)

#Reshape rows, columns
more_nums = nums.reshape(2, 5)
print(more_nums)

print(np_matrix[0])     #Row
print(np_matrix[:,0])   #Column
print(np_matrix[0:,1])   #Slice

 