#WORD COMPRESSION WORKS GOES OVER TIME LIMIT
def findSequence(word, k):
    if len(word) <= k: 
        return -1
    
    #Get each possible sequence of length k
    for i in range(0, len(word)-k+1):
        #'Correct' sequence of all starting letter length k
        sequence = ""
        for _ in range(k):
            sequence += word[i]
        #Compare sequence of length k to correct sequence
        curr = word[i:i+k]
        #If match, return index of start of sequence
        if curr == sequence:
            return i
    return -1

def compressWord(word, k):
    #Check for a row of consecutive letters
    start = findSequence(word, k)
    
    #While there are consecutive letters, continue to remove
    while start != -1:
        word = word[:start] + word[start+k:]
        start = findSequence(word, k)
    
    return word

#WORKS, SLOWER THAN OTHER
def findSequence(word, k):
    sequences = []
    if len(word) <= k: 
        return sequences
    i = 0
    #Start with each letter in word from 0 to len(word)-k
    while i < len(word)-k+1:
        end = i
        #Find last consecutive same letter
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                end = j
            else:
                break

        #Find endpoint
        if end != i and end-i+1 >= k:
            iterations = (end-i+1)//k
            end = i+iterations*k-1
            sequences.append([i, end])
            i = end+1
        else:
            i += 1
                     
    return sequences

def compressWord(word, k):
    #Check for a string of consecutive letters
    endpoints = findSequence(word, k)

    #While there are consecutive letters, continue to remove
    while endpoints != []:
        curr = endpoints.pop()
        word = word[:curr[0]] + word[curr[1]+1:]
        endpoints = findSequence(word, k)
    
    return word










# Is there ever a case where changing the 2 biggest letters will not work?
# Is there ever a case where changing the biggest by 1 won't work, but changing the second biggest by 1 is less effective?
# I think you should only ever need the 2 biggest letters?
# Actually I think you should be able to change the first non-a letter to b unless 

def alphaNumeric(word):
    total = 0
    for i in word:
        total += ord(i)
    return total

def largestLetter(word, exclude):
    largest = 0
    for ind, val in enumerate(word):
        if ind not in exclude:
            if val >= word[largest]: largest = ind
    return largest
    
#Impossible for length 1
if len(palindromeStr) == 1:
    return "IMPOSSIBLE"

#Impossible if all letters are 'a'
allA = ""
for _ in range(len(palindromeStr)):
    allA += 'a'
if palindromeStr == allA:
    return "IMPOSSIBLE"

#Else, check for "largest" letter, and try to convert to 'a'. If the result is a palindrome, try both changing the largest letter to b, as well as the second largest letter to a...
exclude = []
largest = largestLetter(palindromeStr, exclude)
exclude.append(largest)
newWord = palindromeStr[:largest] + 'a' + palindromeStr[largest+1:]

#Make sure newWord isn't a palindrome and is alphanumerically higher
if not isPalindrome(newWord) and alphaNumeric(newWord) > alphaNumeric(palindromeStr):
    return newWord
else:
    
    

#Create alphabet
possible = []
alphabet = []
for i in range(97, 123):
    alphabet.append(chr(i))

#Try all solutions
print(alphabet)
for i in palindromeStr:
    pass


#Else, check for "largest" letter, and try to convert to 'a'. If the result is a palindrome, try both changing the largest letter to b, as well as the second largest letter to a...
exclude = []
largest = largestLetter(palindromeStr, exclude)
exclude.append(largest)
newWord = palindromeStr[:largest] + 'a' + palindromeStr[largest+1:]

#Make sure newWord isn't a palindrome and is alphanumerically higher
if not isPalindrome(newWord) and alphaNumeric(newWord) > alphaNumeric(palindromeStr):
return newWord
else: