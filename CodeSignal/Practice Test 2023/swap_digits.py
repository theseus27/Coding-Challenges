"""
You are given an array of non-negative integers numbers. You are allowed to choose any number from this array and swap any two digits in it. If after the swap operation the number contains leading zeros, they can be omitted and not considered (eg: 010 will be considered just 10).

Your task is to check whether it is possible to apply the swap operation at most once, so that the elements of the resulting array are strictly increasing.
"""

# Final Cleanest Solution
def all_variants(num):
    res = []
    numstr = str(num)
    numarr = [numstr[i] for i in range(len(numstr))]
    
    for i in range(len(numarr)):
        for j in range(len(numarr)):
            newarr = [numarr[i] for i in range(len(numarr))]
            newarr[i], newarr[j] = newarr[j], newarr[i]
            res.append(int(''.join([str(newarr[i]) for i in range(len(newarr))])))
            
    return set(res)

def solution(numbers):
    swapped = False
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            if swapped:
                return False
            
            swapped = True
            prior = 0 if i == 0 else numbers[i-1]
            valid_swap = False
            
            variations_1 = all_variants(numbers[i])
            
            
            for v in variations_1:
                if v > prior and v < numbers[i+1]:
                    valid_swap = True
                    
            if not valid_swap and i < len(numbers)-2:
                variations_2 = all_variants(numbers[i+1])
                for v in variations_2:
                    if v > numbers[i] and v < numbers[i+2]:
                        valid_swap = True
                        
            if not valid_swap:
                return False
    return True


# Working Solution
def all_variants(num):
    res = []
    numstr = str(num)
    numarr = [numstr[i] for i in range(len(numstr))]
    
    for i in range(len(numarr)):
        for j in range(len(numarr)):
            newarr = [numarr[i] for i in range(len(numarr))]
            newarr[i], newarr[j] = newarr[j], newarr[i]
            newstr = ""
            for elt in newarr:
                newstr += str(elt)
            res.append(int(newstr))
            
    return set(res)

def solution(numbers):
    swapped = False
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            if swapped:
                return False
            
            swapped = True
            prior = 0 if i == 0 else numbers[i-1]
            valid_swap = False
            
            variations_1 = all_variants(numbers[i])
            for v in variations_1:
                if v > prior and v < numbers[i+1]:
                    valid_swap = True
                    
            if not valid_swap and i < len(numbers)-2:
                variations_2 = all_variants(numbers[i+1])
                for v in variations_2:
                    if v > numbers[i] and v < numbers[i+2]:
                        valid_swap = True
                        
            if not valid_swap:
                return False
    return True


# Works bu times out on some
# def all_variants(num):
#     res = []
#     numstr = str(num)
#     numarr = [numstr[i] for i in range(len(numstr))]
    
#     for i in range(len(numarr)):
#         for j in range(len(numarr)):
#             newarr = [numarr[i] for i in range(len(numarr))]
#             newarr[i], newarr[j] = newarr[j], newarr[i]
#             newstr = ""
#             for elt in newarr:
#                 newstr += str(elt)
#             res.append(int(newstr))
            
#     return res

# def solution(numbers):
#     swapped = False
#     for i in range(len(numbers)-1):
#         if numbers[i] > numbers[i+1]:
#             if swapped:
#                 return False
            
#             swapped = True
#             prior = 0
#             if i != 0:
#                 prior = numbers[i-1]
            
#             variations = all_variants(numbers[i])
#             valid_swap = False
            
#             for v in variations:
#                 if v > prior and v < numbers[i+1]:
#                     valid_swap = True
#             if not valid_swap:
#                 return False
#     return True
            