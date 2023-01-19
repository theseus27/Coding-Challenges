def order(l):
    if len(l) == 0:
        return 0
    if sum(l) == 0:
        return 0
    l = sorted(l, reverse=True)
    s = ""
    for i in range(len(l)):
        s += str(l[i])
    return int(s)

def solution(l):
    l = sorted(l)
    if (sum(l) % 3 == 0):
        return order(l)

    if (sum(l) % 3 == 1):
        for i in range(len(l)):
            if (l[i] % 3 == 1):
                l.remove(l[i])
                return order(l)
        first = -1
        for i in range(len(l)):
            if (l[i] % 3 == 2):
                if first == -1:
                    first = l[i]
                else:
                    l.remove(first)
                    l.remove(l[i])
                    return order(l)
    
    if (sum(l) % 3 == 2):
        for i in range(len(l)):
            if (l[i] % 3 == 2):
                l.remove(l[i])
                return order(l)
        first = -1
        for i in range(len(l)):
            if (l[i] % 3 == 1):
                if first == -1:
                    first = l[i]
                else:
                    l.remove(first)
                    l.remove(l[i])
                    return order(l)
    return 0


print(solution([3,1,4,1]))
print(solution([3,1,4,1,5,9])) #94311


# Keep 6 to 3 in each list

# EX
# ones = [7,7,7,7]
# twos = [2,2,2,2,2,2]
# Option 1: 7,7,7,2,2,2,2,2,2
# Option 2: 2,7,2,7,2,7,2,7
# Maximize Groups of 3
