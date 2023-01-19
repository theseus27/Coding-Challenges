def solution(l):
    three = sorted([l[i] for i in range(len(l)) if l[i] % 3 == 0], reverse=True)
    two = sorted([l[i] for i in range(len(l)) if l[i] % 3 == 1], reverse=True)
    one = sorted([l[i] for i in range(len(l)) if l[i] % 3 == 2], reverse=True)

    answer = [three[i] for i in range(len(three))]

    while (len(two) >= 3):
        answer.append(two.pop())
        answer.append(two.pop())
        answer.append(two.pop())

    while (len(one) >= 3):
        answer.append(one.pop())
        answer.append(one.pop())
        answer.append(one.pop())

    while (len(one) > 0 and len(two) > 0):
        answer.append(one.pop())
        answer.append(two.pop())

    if len(answer) == 0:
        return 0

    answer = sorted(answer, reverse=True)
    s = ""
    for i in range(len(answer)):
        s += str(answer[i])
    return int(s)

print(solution([3,1,4,1])) #4311
print(solution([3,1,4,1,5,9])) #94311