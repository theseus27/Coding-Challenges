def solution(a):
    #Stringify all the numbers
    numstring = ""
    for i in a:
        numstring += str(i)
    
    occurenceArray = [0 for _ in range(10)]
    for num in numstring:
        num = int(num)
        occurenceArray[num] += 1
    
    mostFrequent = 0
    for i in occurenceArray:
        if i > mostFrequent:
            mostFrequent = i
    
    final = []
    for ind, val in enumerate(occurenceArray):
        if val == mostFrequent:
            final.append(ind)
            
    return final