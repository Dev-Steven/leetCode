def balancedStringSplit(s):
    balStr_ctr = 0
    ctr = 0
    for subStr in s:
        if subStr == 'L':
            ctr += 1
        if subStr == 'R':
            ctr -= 1
        if ctr == 0:
            balStr_ctr += 1
    print(balStr_ctr)
    return balStr_ctr

s = "LLLLRRRR"
balancedStringSplit(s)