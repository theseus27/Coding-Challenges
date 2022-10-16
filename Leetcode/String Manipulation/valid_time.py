def solution(time):
    if len(time) != 5: return False
    hour, colon, min = int(time[:2]), time[2], int(time[3:])
    return hour in range(0,24) and colon == ':' and min in range(0,60)

#Other solutions
import time
h,m=map(int,time.split(":"))
return 0<=h<24 and 0<=m<60

return int(time[0:2]) < 24 and int(time[3:]) < 60
    
#This also kinda works, except it doesn't account for the math of making sure hour is between 0-24 and min is between 0-60
import re
return bool(re.match('[0-2]+[0-9]+\:+[0-5]+[0-9]', time))