def checkString(substring, string):
    occurences = 0
    used = []
    for i in range (0, len(string)-len(substring)+1):
        if (i in used):
            continue
        if (string[i:i+len(substring)] == substring): 
            occurences += 1
            for j in range(i, i+len(substring)):
                used.append(j)
    return occurences

def solution(s):
    maxOccurences = 0
    minLeftover = len(s)
    for substringLength in range(1, len(s)+1):
        for substringStart in range(0, len(s)-substringLength+1):
            substringEnd = substringStart + substringLength
            #print("Len: " + str(substringLength) + " Start: " +
                  #str(substringStart) + " End: " + str(substringEnd))
            substring = s[substringStart:substringEnd]
            #print(substring)
            occurences = checkString(substring, s)
            leftover = len(s)-occurences*substringLength
            #print(str(substring) + " " + str(occurences) + " " + str(leftover))
            if (leftover < minLeftover):
                maxOccurences = occurences
                minLeftover = leftover
            elif (leftover == minLeftover):
                if (occurences > maxOccurences):
                    maxOccurences = occurences
            #print(str(maxOccurences) + " " + str(minLeftover))
    return maxOccurences
    
test1 = solution("abcabcabc") #3
print(test1)
test2 = solution("aaabc")   #1
print(test2)
test3 = solution("a")       #1
print(test3)

given1 = solution("abcabcabcabc") #4
given2 = solution("abccbaabccba") #2
print(given1)
print(given2)
