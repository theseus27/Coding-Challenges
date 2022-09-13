def find_cliff(elevations, features, rows, columns):
    allowed = ["R", "T", "W"]
    for i in range(rows):
        for j in range(columns):
            if features[i][j] == "S": return False
        
    for i in range(rows-1):
        for j in range(columns-1):
            if features[i][j] == "R" and features[i][j+1] == "R" and elevations[i][j] == elevations[i][j+1] and elevations[i][j] >= 50:
                if features[i+1][j] in allowed and features[i+1][j+1] in allowed and elevations[i+1][j] == elevations[i+1][j+1]:
                    if elevations[i][j] > elevations[i+1][j] and elevations[i][j+1] > elevations[i+1][j+1]: return True
    return False