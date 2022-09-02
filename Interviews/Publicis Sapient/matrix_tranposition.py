import sys

matrix = []
line_num = 0

input = ["1 2 3", "2 3 4", "5 6 7"]

for line in input:
    nums = line.strip().split(" ")
    
    if line_num == 0:
        for num in nums:
            matrix.append([num])
    else:
        for place in range(len(nums)):
            matrix[place].append(nums[place])
    line_num += 1

for row in matrix:
    row_str = ""
    for num in row:
        row_str += (" " + str(num))
    row_str = row_str[1:]
    print(row_str)