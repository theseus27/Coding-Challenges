#Worked on like 1 lmao
def solution(field, figure):
    columns = len(field[0])
    rows = len(field)
    transposed = []
    for i in range(columns):
        next_row = []
        for j in range(rows):
            next_row.append(field[j][i])
        transposed.append(next_row)
        
    figure_transposed = []
    for i in range(3):
        next_row = []
        for j in range(3):
            next_row.append(figure[j][i])
        figure_transposed.append(next_row)

    #Get deepest position for each column
    deepest = [0 for _ in range(columns)]
    for column in range(columns):
        for row in range(rows):
            if transposed[column][row] == 0:
                deepest[column] = row
            else: break
    
    #Get depth of piece per column
    piece_depth = [0 for _ in range(3)]
    for column in range(3):
        for row in range(3):
            if transposed[column][row] == 0:
                piece_depth[column] = row
            else: break
    
    #See how deep the piece can get in a column
    piece_max_depth = 0
    for i in range(columns):
        column_depth = 0
        for j in range(rows):
            if piece_depth[i] + deepest[i]: column_depth = j
        
        #See if a row has been completed
        for k in range(3):
            if k+j < rows:
                for l in range(3):
                    if i+l < columns:
                        field[j+k][i+l] = figure[k][l]
                
        for m in range(rows):
            if sum(field[m]) == rows:
                return column
             
    return -1


#Edge cases where it would go 'off the map'
if column == -2:
    if sum(figure.transpose[0] != 0 or sum(figure.transpose[1]) != 0):
        pass    #Continue
if column == -1:
    if sum(figure.transposed[0] != 0):
        pass    #Continue
if column == columns:
    if sum(figure.transpose[2] != 0):
        pass    #Continue
if column == columns+1:
    if sum(figure.transpose[2] != 0 or sum(figure.transpose[1] != 0)):
        pass    #Continue