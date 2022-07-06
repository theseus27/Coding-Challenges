import numpy as np

def follow(path, done, termStates, matrix):
    print("Following path: " + str(path))
    thisState = path[len(path)-1]
    if (thisState in termStates):
        return path, True

    for nextState in matrix[thisState]:
        if ((nextState) != 0):
            path += (", " + str(thisState))
            follow(path, done, termStates, matrix)

    return path, False

def solution(m):
    matrix = np.array(m, dtype=int)
    dimension = len(matrix)
    
    #Get Terminal States
    for index, value in enumerate(matrix):
        terminalStates = []
        isTerminal = True
        for j in value:
            if (j != 0):
                isTerminal = False
        if (isTerminal == True):
            terminalStates.append(index)
    if (0 in terminalStates):
        return [1, 1]
    
    #Find Possible Routes
    possibleRoutes = []
    for firstState in matrix[0, :]:
        #Might Have to turn each row into it's own array or something idk
        print(firstState)
        if (firstState != 0):
            thisPath = [0, firstState]
            done = False
            while (done == False):
                thisPath, done =  follow(thisPath, done, terminalStates, matrix)
            if (thisPath not in possibleRoutes):
                possibleRoutes.append(thisPath)
    return possibleRoutes
    
sol = solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
print(sol)
