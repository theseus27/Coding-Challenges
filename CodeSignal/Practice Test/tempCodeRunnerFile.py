    # for i in range(columns-2):
    #     for j in range(rows-2):
    #         field_slice = [[field[j][i], field[j][i+1], field[j][i+2]], [field[j+1][i], field[j+1][i+1], field[j+1][i+2]], [field[j+2][i], field[j+2][i+1], field[j+2][i+2]]]
    #         if overlap(figure, field_slice) & check_above(figure, field, i, j):
    #             if row_completion(figure, field, i, j):
    #                 return i
    # return -1