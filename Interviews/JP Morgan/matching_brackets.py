def balance(exp, rep):
    left = 0; right = 0
    for i in exp:
        if i == "<": left += 1
        else: 
            if left > 0: left -= 1
            else: right += 1
            
    if right - rep <= 0 and left == 0: return True
    return False

def canBalance(expressions, repairs):
    results = [0 for i in range(len(expressions))]
    for i in range(len(expressions)):
        if balance(expressions[i], repairs[i]):
            results[i] = 1
    return results

expressions = ["<<>>", "<<>", ">>>", "<>><", "<>>", "><>>", "<<>>>"]
repairs = [0, 1, 2, 2, 1, 1, 1]
print(canBalance(expressions, repairs))