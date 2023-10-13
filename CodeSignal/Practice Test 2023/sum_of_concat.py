"""
Given an array of positive integers a, your task is to calculate the sum of every possible a[i] ∘ a[j], where a[i] ∘ a[j] is the concatenation of the string representations of a[i] and a[j] respectively.

For a = [10, 2], the output should be solution(a) = 1344.
a[0] ∘ a[0] = 10 ∘ 10 = 1010,
a[0] ∘ a[1] = 10 ∘ 2 = 102,
a[1] ∘ a[0] = 2 ∘ 10 = 210,
a[1] ∘ a[1] = 2 ∘ 2 = 22.
"""

def solution(a):
    res = 0
    num_of_len = [0 for _ in range(7)]
    
    for num in a:
        num_of_len[len(str(num)) - 1] += 1

    multiplier = sum([num_of_len[i] * pow(10, i+1) for i in range(7)]) + len(a)
    
    a_sum = sum(a)
    
    return a_sum*multiplier

# Working solution, more verbose
# def solution(a):
#     res = 0
    
#     len1 = []
#     len2 = []
#     len3 = []
#     len4 = []
#     len5 = []
#     len6 = []
#     len7 = []
    
#     for num in a:
#         if num < 10:
#             len1.append(num)
#         elif num < 100:
#             len2.append(num)
#         elif num < 1000:
#             len3.append(num)
#         elif num < 10000:
#             len4.append(num)
#         elif num < 100000:
#             len5.append(num)
#         elif num < 1000000:
#             len6.append(num)
#         else:
#             len7.append(num)
    
#     for num in a:
#         isum = num*(len(len1)*10 + len(len2)*100 + len(len3)*1000 + len(len4)*10000 + len(len5)*100000 + len(len6)*1000000 + len(len7)*10000000)
#         jsum = num*len(a)
#         res += (isum + jsum)
    
#     return res


# Notes 
    """
    [25, 1, 2, 3]
    
    251 + 252 + 253
    125 + 225 + 325
    12 + 13 + 23 + 21 + 31 + 32
    
    when a number is i, it's i*len(len1)*10 + i*len(len2)*100 + ...
    when a number is j, it's j
    """
    
    
    # res = 0
    
    # for i in range(len(a)):
    #     for j in range(len(a)):
    #         num = int(str(a[i]) + str(a[j]))
    #         res += num
    
    # return res