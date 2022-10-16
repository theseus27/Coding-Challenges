import re
def solution(text):
    #^ means not in
    return max(re.split('[^a-zA-Z]', text), key=len)
print(solution("Hi this is, Theseus!"))

# #Mine
# alpha = [chr(i) for i in range(97,123)] + [chr(i) for i in range(65,91)]
# longest = ""
# curr = ""
# for i in text:
#     print(curr)
#     if i in alpha:
#         curr += i
#     if len(curr) >= len(longest):
#             longest = curr
#     if i not in alpha:
#         curr = ""
        
# return longest
