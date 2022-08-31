#Given a line length and array of strings, center the text and fit as many strings on a line as you can, but can't split a string across lines
#Surround text block with stars on sides and top/bottom
#If there's an extra space, put it on the right

def format(length, paragraph):
    #Split into lines
    formatted = ['']
    for line in paragraph:
        if len(line) + 1 < length - len(formatted[-1]):
            formatted[-1] += (" " + line)
        else:
            formatted.append(line)
    formatted[0] = formatted[0][1:]
    
    #Add spacing
    for i in range(len(formatted)):
        spaces = length-len(formatted[i])
        front_space = ""; back_space = ""
        for _ in range(spaces//2): 
            front_space += " "
            back_space += " "
        if spaces%2 == 1:
            back_space += " "
        formatted[i] = front_space + formatted[i] + back_space
            
    #Add top and bottom border
    border = ""    
    for _ in range(length):
        border += "*"
    formatted.insert(0, border)
    formatted.append(border)
    
    #Add outer borders
    for i in range(len(formatted)):
        formatted[i] = "*" + formatted[i] + "*"
    
    for line in formatted:
        print(line)
        
    
    
(format(12, ["this is", "an example", "of an array", "to", "be", "formatted"]))