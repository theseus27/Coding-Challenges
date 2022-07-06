def solution(x):
    newString = ""
    for letter in x:
        if ((ord(letter) >= 97) and (ord(letter) <= 122)):
            newLetter = 219-ord(letter)
            letter = chr(newLetter)
            newString += str(letter)
        else:
            newString += letter
    return newString

#Test
    #mySolution = solution("Yearb")
    #print(mySolution)