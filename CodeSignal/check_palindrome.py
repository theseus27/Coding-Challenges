def solution(inputString):
    #[::-1] reverses it
    return inputString == inputString[::-1]

#My Way
# for i in range(len(inputString)//2):
#     if inputString[i] != inputString[len(inputString)-1-i]:
#         return False
# return True