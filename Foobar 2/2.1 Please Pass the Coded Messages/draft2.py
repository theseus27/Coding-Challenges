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
    three = sorted([l[i] for i in range(len(l)) if l[i] % 3 == 0], reverse=True)
    two = sorted([l[i] for i in range(len(l)) if l[i] % 3 == 1], reverse=True)
    one = sorted([l[i] for i in range(len(l)) if l[i] % 3 == 2], reverse=True)

    if (len(two) == len(one) or abs(len(two)-len(one)) % 3 == 0):
        return order(l)
    elif(len(two) > len(one)):
        longer = two
        shorter = one
    else:
        longer = one
        shorter = two

    answer = [three[i] for i in range(len(three))]

    while(len(shorter) > 3):
        answer.append(longer.pop())
        answer.append(longer.pop())
        answer.append(longer.pop())
        answer.append(shorter.pop())
        answer.append(longer.pop())
        answer.append(longer.pop())


    
    return order(answer)

print(solution([3,1,4,1]))
print(solution([3,1,4,1,5,9])) #94311


# Keep 6 to 3 in each list

# EX
# ones = [7,7,7,7]
# twos = [2,2,2,2,2,2]
# Option 1: 7,7,7,2,2,2,2,2,2
# Option 2: 2,7,2,7,2,7,2,7
# Maximize Groups of 3
