# Passes 1, 2, 3, 4

#Global Variables
finalList = [-1, -1]
start = 0
end = -1
currSum = 0

#See if the indices should be replaced
def newList(l):
    global finalList
    global start
    global end
    global currSum
    if (finalList == [-1, -1]):
        finalList = [start, end]
        currSum -= l[start]
        start += 1
    else:
        if (finalList[1]-finalList[0] > end-start):
            finalList = [start, end]
            currSum -= l[start]
            start += 1

def solution(l, t):
    global finalList
    global start
    global end
    global currSum
    finalList = [-1, -1]
    start = 0
    end = -1
    currSum = 0
    
    for i in l:
        currSum += i
        end += 1
        if (currSum == t):
            newList(l) 
        elif (currSum > t):
            while (currSum > t):
                currSum -= l[start]
                start += 1
            if (currSum == t):
                newList(l)
    return finalList


"""
# Longer solution followed by shorter solution
sol1 = solution([4, 3, 5, 7, 8], 12)
print(sol1)

# No solution
sol2 = solution([1, 2, 3], 7)
print(sol2)

# 2 solutions
sol3 = solution([4, 5, 6, 3, 6], 9)
print(sol3)

# Shorter solution followed by longer solution
sol4 = solution([5, 7, 1, 2, 2], 12)
print(sol4)

# First number is the solution
sol5 = solution([5, 4, 3], 5)
print(sol5)

# Last number is the solution
sol6 = solution([1, 2, 3, 10], 10)
print(sol6)

# Last 2 numbers are the solution
sol7 = solution([1, 4, 3, 9, 2, 6], 8)
print(sol7)

# Index out on last one
sol8 = solution([1, 4, 6, 7], 5)
print(sol8)

sol9 = solution([1, 2, 1, 10, 7], 11)
print(sol9)
"""