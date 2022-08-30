def valid_ip(ipaddress):
    if ipaddress.count(".") != 3:
        return "Invalid"
    nums = ipaddress.split(".")
    for num in nums:
        if int(num) >= 0 and int(num) <= 255:
            continue
        else:
            return "Invalid"
    return "Valid"

print(valid_ip(".."))
print(valid_ip("1.1.1.1"))
print(valid_ip("256.1.2.3"))
