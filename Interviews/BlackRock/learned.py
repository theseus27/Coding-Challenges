#                 GENERAL PROGRAMMING

#Recursion
def recurse(start, end, current_value):
    if something == something:
        #global_variable.append(current_value)
        return
        #etc
    else:
        #do something to get a new start
        #do something to current_value
        recurse(new_start, start, current_value)
        

#                       SYNTAX
word = "hi.i.am.theseus"
listname = []
word.split(".") #Splitting on character
word.strip()    #Removing whitespace
listname.sort(reverse=True) #Sort list
word.capitalize() #Capitalize word

import sys      #Reading in from stdin
#for line in sys.stdin | sys.stdin.readline()


#                       CONCEPTS
#Negative indexing  (left side is NOT inclusive, right side IS)
word = "hello"
word[:-1]    # = "hell"
word[-1:]    # = "o"

#Tuples
tupleList = [(1, True, "a"), (2, False, "b")]
tupleList[0][1] # = True