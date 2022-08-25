#Input: string in 12 hour time
#Output: string in 24 hour time

def timeConversion(s):
    ampm = s[-2:]
    if ampm == "AM":
        if (s[:2] == "12"):
            return "00" + s[2:-2]
        else:
            return s[:-2]
    else:
        hour = s[:2]
        if (hour != "12"):
            hour = int(hour) + 12
        return str(hour) + s[2:-2]

print(timeConversion("07:45:00PM"))
print(timeConversion("07:45:00AM"))