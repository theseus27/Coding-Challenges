#Power doesn't matter
#Even ** anything = even
#Odd ** anything = odd

#Even * anything = even
#Odd * odd = odd

def solve(m, string_array):
    even = 0
    
    for string in string_array:
        has_even = False
        for letter in string:
            if has_even == False:
                if ord(letter) % 2 == 0:
                    even += 1
                    has_even = True
                
      
    if (len(string_array)-even)%2 == 0:
        return "EVEN"
    return "ODD"


#LONG WAY
def solve(m, s):
    total = 0
    for string in s:
        string_powers = [ord(letter)**m for letter in string]
        product = 1
        for j in string_powers:
            product = product * j
        total += product
    
    if product%2 == 0:
        return "EVEN"
    else:
        return "ODD"