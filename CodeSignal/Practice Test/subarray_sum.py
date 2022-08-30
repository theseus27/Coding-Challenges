def find_pair(subarray, m, k):
    for x in range(m):
        for y in range(m):
            if x == y: continue
            if subarray[x] + subarray[y] == k:
                return 1
    return 0

def solution(a, m, k):
    solutions = 0
    for i in range(0, len(a)-m+1):
        subarray = a[i:i+m]
        solutions += find_pair(subarray, m, k)
                    
    return solutions
        
print(solution([2, 4, 7, 5, 3, 5, 8, 5, 1, 7], 4, 10))  #5
print(solution([15, 8, 8, 2, 6, 4, 1, 7], 2, 8))        #2