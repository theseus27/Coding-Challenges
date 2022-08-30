#Compress word takes string word and int k (number of consecutive equal chars)
#The final word will be unique (abbc == azzc)?
#k will always be the same

#abbcccb 3-> a
#abbbcca 2-> aba
#abbbcca 3-> acca

#Does it do all the removals at once or one at a time?
#caaaacddddcc -> ""
#cccccccddddcb -> b

def findSequence(word, k):
    if len(word) <= k: 
        return [-1, -1]
    
    #Start with each letter in word from 0 to len(word)-k
    for i in range(0, len(word)-k+1):
        end = i
        
        #Find last consecutive same letter
        for j in range(i, len(word)):
            if word[i] == word[j]:
                end = j
            else:
                break

        #Find endpoint
        if end != i and end-i+1 >= k:
            iterations = (end-i+1)//k
            end = i+iterations*k-1
            return [i, end]
                     
    return [-1, -1]

def compressWord(word, k):
    #Check for a string of consecutive letters
    endpoints = findSequence(word, k)

    #While there are consecutive letters, continue to remove
    while endpoints != [-1, -1]:
        word = word[:endpoints[0]] + word[endpoints[1]+1:]
        endpoints = findSequence(word, k)
    
    return word

print(compressWord('abbcccb', 3))