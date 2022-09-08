def solution(A):
    maximum = -1
    arr_string = ""
    for i in A:
        arr_string += (str(i) + ",")
    arr_string = arr_string[:-1]
    sections = arr_string.split("-")
    print(sections)
    
    for idx, val in enumerate(sections):
        section_sum = 0
        nums = val.split(",")
        if idx != 0:
            nums = nums[1:]
        for num in nums:
            if num != '':
                section_sum += int(num)
        if (section_sum > maximum and section_sum != 0):
            maximum = section_sum
    
    return maximum

result = solution([1,-1,2,3,-2,4])
result = solution([])
result = solution([-2])
print(result)