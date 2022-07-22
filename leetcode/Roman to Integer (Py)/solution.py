class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        prev = ""

        for index, curr in enumerate(s):
            if (prev == "I"):
                if (curr == "V"):
                    s = s[0:index-1:] + "aa" + s[index+1::]
                    total += 4
                elif (curr == "X"):
                    s = s[0:index-1:] + "aa" + s[index+1::]
                    total += 9
            elif (prev == "X"):
                if (curr == "L"):
                    s = s[0:index-1:] + "aa" + s[index+1::]
                    total += 40
                elif (curr == "C"):
                    s = s[0:index-1:] + "aa" + s[index+1::]
                    total += 90
            elif (prev == "C"):
                if (curr == "D"):
                    s = s[0:index-1:] + "aa" + s[index+1::]
                    total += 400
                elif (curr == "M"):
                    s = s[0:index-1:] + "aa" + s[index+1::]
                    total += 900
            prev = curr

        for i in s:
            if (i == "I"):
                total += 1
            elif (i == "V"):
                total += 5
            elif (i == "X"):
                total += 10
            elif (i == "L"):
                total += 50
            elif (i == "C"):
                total += 100
            elif (i == "D"):
                total += 500
            elif (i == "M"):
                total += 1000
            elif (i == "a"):
                total += 0
            else:
                exit("Invalid input")

        return total
