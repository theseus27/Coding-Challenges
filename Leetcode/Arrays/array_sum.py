def solution(a):
    b = a.copy()
    
    for index, value in enumerate(a):
        if index == 0:
            prevprev = 0
            prev = value
            continue
            
        if index == len(a) -1:
            b[index-1] = value + prev + prevprev
            b[index] = value + prev
        else:
            b[index-1] = value + prev + prevprev
            prevprev = prev
            prev = value
            
    return b