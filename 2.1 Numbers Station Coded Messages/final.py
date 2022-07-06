def solution(l, t):
    sum = 0
    start = 0
    for end, value in enumerate(l):
        sum += value
        while(sum > t and start < end):
            sum -= l[start]
            start += 1
        if sum == t:
            return [start, end]
    return [-1, -1]
