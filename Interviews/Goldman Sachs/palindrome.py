#Given a palindrome, change one character to meet the following 3 conditions:
    #The new string is lower alphabetically than the initial string
    #The new string is the lowest value alphabetically that can be created
    #The new string is not a palindrome

    #Given string is guaranteed to be a palindrome (all lowercase)
    #Return "IMPOSSIBLE" if not found

def isPalindrome(word):
    halfway = int(len(word) / 2)
    for i in range(0, halfway):
        if word[i] != word[len(word)-i-1]:
            return False
    return True

def breakPalindrome(palindromeStr):
    newWord = "IMPOSSIBLE"
    #Iterate right to left to ensure 'lowest' resulting string
    #For each letter in given string, check that the letter is not a
    for ind in range(len(palindromeStr)-1, -1, -1):
        if palindromeStr[ind] != 'a':
            #Create temp string replacing curr letter w/ a and check that result is not palindrome
            hold = palindromeStr[:ind] + 'a' + palindromeStr[ind+1:]

            if not isPalindrome(hold):
                newWord = hold
                
    return newWord
    
print(breakPalindrome("mom"))
print(breakPalindrome("kayak"))
print(breakPalindrome("boob"))
print(breakPalindrome("bzb"))
print(breakPalindrome("b"))
print(breakPalindrome("a"))
print(breakPalindrome("aza"))
print(breakPalindrome("aazaaa"))
