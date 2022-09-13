def findMinimumCost(n, elevations):
    rows = len(elevations)
    columns = len(elevations[0])
    
    #Create matrix of sums up to each point
    sums = [elevations[0]]
    for _ in range(rows-1):
        sums.append([])
    #Add Columns
    for i in range(1, rows):
        for j in range(columns):
            sums[i].append(sums[i-1][j] + elevations[i][j])
    #Add Rows
    for i in range(1, columns):
        for j in range(rows):
            sums[j][i] += sums[j][i-1]
    #Add buffers
    sums.insert(0, [0 for _ in range(columns)])
    for i in range(rows+1):
        sums[i].insert(0, 0)
        
    #Find smallest subarray   
    min_area = 10**10
    for i in range(1, rows-n+2):
        for j in range(1, columns-n+2):
            subarray = sums[i+n-1][j+n-1] - sums[i-1][j+n-1] - sums[i+n-1][j-1] + sums[i-1][j-1]
            if subarray < min_area: min_area = subarray
    return(min_area)
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    elevations_rows = int(input().strip())
    elevations_columns = int(input().strip())

    elevations = []

    for _ in range(elevations_rows):
        elevations.append(list(map(int, input().rstrip().split())))

    result = findMinimumCost(n, elevations)

    fptr.write(str(result) + '\n')

    fptr.close()
