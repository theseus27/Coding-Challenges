def solution(l):
    nums = sorted(l, reverse=True)

    if (sum(nums) % 3 == 0):
        s = ""
        for i in range(len(nums)):
            s += str(nums[i])
        return int(s)

    answers = [0]
    for i in range(len(nums)):
        minus_one = [nums[x] for x in range(len(nums))]
        minus_one.pop(i)
        if (sum(minus_one) % 3 == 0):
            s = ""
            for k in range(len(minus_one)):
                s += str(minus_one[k])
                answers.append(int(s))
        for j in range(len(minus_one)):
            minus_two = [minus_one[x] for x in range(len(minus_one))]
            minus_two.pop(j)
            if (sum(minus_two) % 3 == 0):
                s = ""
                for k in range(len(minus_two)):
                    s += str(minus_two[k])
                    answers.append(int(s))

    return max(answers)

print(solution([3,1,4,1]))
print(solution([3,1,4,1,5,9])) #94311
