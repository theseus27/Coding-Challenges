#Each parenthesis (, [, { is closed
#( )    must match on the same line
# There will only be one or two parentheses on each line
#Input: str, output: bool

import sys

def check_parentheses() -> bool:
    pending = ""    #String of open parentheses waiting to be closed
    curve_pending = False    #Tracks if there is an open parentheses 
                             #    that needs to be closed on that line
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    
    for line in sys.stdin:
        for char in line:
            #If opening parenthesis, update variables
            if char in opening: pending += char
            if char == '(': curve_pending = True
            
            #If closing parenthesis, check variables to see if it should be there,
            #    and update variables if so
            if char in closing:
                if pending == "": return False
                else:
                    if char == ')':
                        if pending[-1] == '(': 
                            pending = pending[:-1]
                            curve_pending = False
                        else: return False
                    elif char == ']':
                        if pending[-1] == '[': pending = pending[:-1]
                        else: return False
                    elif char == '}':
                        if pending[-1] == '{': pending = pending[:-1]
                        else: return False
        #Check for an unclosed curved parenthesis on that line
        if curve_pending:
            return False
            
    #When input is done, check for any remaining unclosed parenthesis
    if pending == "": return True
    else: return False

def main():
    valid = check_parentheses()
    if valid:
        print("valid")
    else:
        print("invalid")

if __name__ == "__main__":
    main()