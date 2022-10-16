#After partitioning, sort earch partition in ascending order. Concatenate the sorted partitions and compare to resulting array of original array sorted. If match, valid.
#EX. [2, 10, 5, 9] --> 2
#EX. [2, 1, 3, 2, 4, 4, 5, 8, 7, 7] --> 6

#ATTEMPT 1
# def findSubs(arr):
#     if arr[-1] >= max(arr[:-1]):
#         return [arr[:-1]]
#     if arr[0] <= min(arr[1:]):
#         return [arr[1:]]
#     for i in range(1, len(arr)-1):
#         if max(arr[:i+1]) <= min(arr[i:]):
#             return [arr[:i+1], arr[i+1:]]
#     return []
# def findMaxSubsegmentsCount(arr):
#     numSecs = 0
#     subsecs = [arr]
#     it = 0
#     while len(subsecs) > it:
#         sec = subsecs[it]
#         if len(sec) > 1:
#             numSecs += 1
#             moreSec = findSubs(sec)
#             if len(moreSec) == 2:
#                 subsecs.append(moreSec[0])
#                 subsecs.append(moreSec[1])
#             elif len(moreSec) == 1:
#                 subsecs.append(moreSec[0])
#         it += 1
#     return numSecs

def findMaxSubsegmentsCount(arr):
    count = 1
    for i in range(1, len(arr)):
        if (arr[i] >= max(arr[:i])):
            count += 1
    return count

print(findMaxSubsegmentsCount([2, 1, 3, 2, 4, 4, 5, 8, 7, 7]))
print(findMaxSubsegmentsCount([2, 10, 5, 9]))