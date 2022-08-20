#GIVEN: exchange rates, currency to convert, currency to convert to
#Calculate max amount of target to 1 unit of selected currency
    #If you can't complete, return -1.0
    
import sys

possible = [-1.0]    #Possible exchange results
conv = []            #Conversions as tuples

#Calculate all possible results recursively
def find_conv(start, end, curr):
    if start == end:
        possible.append(curr)
    else: #Find paths to follow
        for i in conv:
            if i[0] == start:
                find_conv(i[1], end, curr*i[2])

def main():
   #Parse exchange rates into list then append to conv as tuple
    conversion_string = sys.stdin.readline().strip()
    conversion_list = conversion_string.split(";")
    for i in conversion_list:
        prop = i.split(",")
        conv.append((prop[0], prop[1], float(prop[2])))
    #Get selected and target currencies
    selected = sys.stdin.readline().strip()    #Can just do readline from consistency of input
    target = sys.stdin.readline().strip()
    
    #Recursively find all possible conversion paths
    find_conv(selected, target, 1)
    
    #Print best conversion rate
    possible.sort(reverse=True)
    print(possible[0])     

if __name__=="__main__":
    main()

#Testing
"""
print("Conversions: " + str(conv))
print("Selected: " + str(selected))
print("Target: " + str(target))
print("Finding conversions from " + start + " to " + end)
"""