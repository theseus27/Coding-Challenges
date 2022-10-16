#Return length/width of biggest square of all defective products (marked with a 1)
#Given a square array nxn where n in [0, 500]
#First line of input is n

def findLargestSquareSize(samples):
    # n = len(samples)
    # largestSize = 0
    # for i in range(n):
    #     for j in range(n):
    #         currSize = 0
    #         if samples[i][j] == 1:
    #             square = True
    #             while (square and i+currSize < n and j + currSize < n):
    #                 for k in range(currSize):
    #                     if samples[i][j+k] == 0: square = False
    #                     if samples[i+k][j] == 0: square = False
    #                 if samples[i+currSize][j+currSize] == 0: square = False
    #                 if square: currSize += 1
    #         if currSize > largestSize: largestSize = currSize
    # return largestSize
    
    n = len(samples)
    largestSize = 0
    for i in range(n):
        if sum(samples[i]) == 0: continue
        j = 0
        currSize = 0
        while j < n:
            reset = False
            if samples[i][j] == 0: reset = True
            else:
                if j + currSize >= n or i + currSize >= n: reset = True
                else:
                    for k in range(currSize):
                        if samples[i][j+k] == 0: reset = True
                        if samples[i+k][j+currSize] == 0: reset = True
           
            if reset == False:
                currSize += 1
                j += 1
            else:  
                if currSize > largestSize: largestSize = currSize
                currSize = 0
                j += 1            
    return largestSize

if __name__ == '__main__':
    samples=[[1,1,1],[1,1,0],[1,0,1]] #Should return 2
    result = findLargestSquareSize(samples)
    print(str(result))

