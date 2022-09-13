def findHighestElevation(elevations):
    highest = 0
    for i in elevations:
        for j in i:
            if j > highest: highest = j
    return highest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    elevations_rows = int(input().strip())
    elevations_columns = int(input().strip())

    elevations = []

    for _ in range(elevations_rows):
        elevations.append(list(map(int, input().rstrip().split())))

    result = findHighestElevation(elevations)

    fptr.write(str(result) + '\n')

    fptr.close()