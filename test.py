#.sort()
nums = [3, 4, 2, 9 ,4 , 5]
nums.sort()
print(nums)

#.sort() w/ a key
tups = [("Jimmy", 20), ("Marco", 21), ("Dax", 19)]
tups.sort(key= lambda x: x[0])
print(tups)

tupnames = [(lambda y: y[0]) in tups]   #Don't need "for y"
tupnames = [(y[0]) for y in tups]       #Doesn't work...returns 1
print(tupnames)

#Index finding
word1, word2 = "helloworld", "ello"
print(word1.index(word2) if word2 in word1 else "")