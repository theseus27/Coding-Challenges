#You are given a string that represents time in the format hh:mm. Some of the digits are blank (represented by ?). Fill in ? such that the time represented by this string is the maximum possible. Maximum time: 23:59, minimum time: 00:00. You can assume that input string is always valid.

def solve(input: str):
    i = [input[j] for j in range(5)]
    
    if i[0] == '?': i[0] = '2' if i[1] == '?' or int(i[1]) < 4 else '1'
    if i[1] == '?': i[1] = '3' if i[0] == '2' else '9'
    if i[3] == '?': i[3] = '5'
    if i[4] == '?': i[4] = '9'
    return ''.join(i)

def solve_long(input: str):
    if input[0] == '?':
        if input[1] == '?':
            input = "23" + input[2:]
        elif int(input[1]) > 3:
            input = "1" + input[1:]
        else:
            input = "2" + input[1:]
    
    if input[1] == '?':
        if input[0] == '2':
            input = input[0] + "3" + input[2:]
        else:
            input = input[0] + "9" + input[2:]
    
    if input[3] == '?':
        input = input[:3] + "5" + input[4:]
    
    if input[4] == '?':
        input = input[:4] + "9"
    return input

print(solve("?4:5?"))
print(solve("23:5?"))
print(solve("2?:22"))
print(solve("0?:??"))
print(solve("??:??"))