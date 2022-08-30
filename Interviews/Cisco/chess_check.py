def can_check(x1, x2, y1, y2):
    if x1 == x2:
        return "Yes"
    if y1 == y2:
        return "Yes"
    if x1+x2 == y1+y2:
        return "Yes"
    if abs(x1-x2) == abs(y1-y2):
        return "Yes"
    return "No"

print(can_check(1,1,2,2))
print(can_check(8, 6, 7, 5))