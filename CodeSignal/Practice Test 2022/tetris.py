def check_above(figure, field, column, row):
    rows = len(field)
    
    #Get deepest position for each column
    column_deepest = [0 for _ in range(3)]
    for i in range(3):
        for j in range(rows):
            if field[j][i] == 0:
                column_deepest[i] = j
            else: break

    #Get depth of piece per column
    piece_deepest = [0 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if figure[j][i] == 0:
                piece_deepest[i] = j
            else: break

    for i in range(3):
        print(column_deepest[i])
        print(piece_deepest[i]+row)
        if column_deepest[i] < piece_deepest[i] + row:
            return False
    return True
        
def overlap(figure, field_slice):
    for i in range(3):
        for j in range(3):
            if figure[i][j] == 1 and field_slice[i][j] == 1:
                return False
    return True

def row_completion(figure, field, column, row):
    columns = len(field[0])      
    for i in range(3):
        if sum(field[i+row]) + sum(figure[i]) == columns:
            return True

    return False

def solution(field, figure):
    rows = len(field)

    ###TESTING
    i = 0
    for j in range(rows-2):
        field_slice = [[field[j][i], field[j][i+1], field[j][i+2]], [field[j+1][i], field[j+1][i+1], field[j+1][i+2]], [field[j+2][i], field[j+2][i+1], field[j+2][i+2]]]
        over = overlap(figure, field_slice)
        print("Overlap: " + str(over))
        above = check_above(figure, field, i, j)
        print("Above: " + str(above))
        completion = row_completion(figure, field, i, j)
        print("Completion: " + str(completion) + "\n")
    
    #Try each column...try each row
    #Check that at each position nothing is 'overlapping' between the grids, and then check if any rows are filled
    # for i in range(columns-2):
    #     for j in range(rows-2):
    #         field_slice = [[field[j][i], field[j][i+1], field[j][i+2]], [field[j+1][i], field[j+1][i+1], field[j+1][i+2]], [field[j+2][i], field[j+2][i+1], field[j+2][i+2]]]
    #         if overlap(figure, field_slice) & check_above(figure, field, i, j):
    #             if row_completion(figure, field, i, j):
    #                 return i
    # return -1

def main():
    #Test Case
    field = [[0,0,0], [0,0,0], [0,0,0], [1,0,0], [1,1,0]]
    figure = [[0,0,1], [0,1,1], [0,0,1]]
    print(solution(field, figure))  # 0

    field = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 1]]
    figure = [[1, 1, 1], [1, 0, 1], [1, 0, 1]]
    #print(solution(field, figure)) # 2
    
if __name__ == "__main__":
    main()