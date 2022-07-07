# Passes 1, 2, 5

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
            currSum -= l[start]
            start += 1
            if (currSum == t):
                newList(l)
    return finalList