#Hash Table
    #Search, Insert, Remove:    O(1) on avg
    
    #In Python, used by sets and dics
    
#Sets
a = set("pikachu")
b = set("theseus")
print(a)            
print(b)
print(a-b)  #Elements in a but not b
print(a|b)  #Elements in a or b or both
print(a&b)  #Elements in a and b
print(a^b)  #Elements in a or b NOT both

#Set comprehension
c = {x for x in a if x not in b}

#Dictionaries
phonebook = {"jake":1111, "matt":2222, "percy": 3333, "luke":4444}
print(phonebook["percy"])
print([(key,value) for key, value in phonebook.items() if str(value)[0] == str(value)[1]])
print(phonebook.keys())
print(phonebook.values())
print(phonebook.items())

#Zip two lists into a dictionary
pokemon = ["pikachu", "bulbasaur", "charmander"]
type = ["electric", "grass", "fire"]
print([(p,t) for p,t in zip(pokemon, type)])
