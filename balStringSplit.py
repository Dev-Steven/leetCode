def balancedStringSplit(s):
    balStr_ctr = 0
    l_ctr = 0
    r_ctr = 0
    for i, v, in enumerate(s):
        if v == 'L':
            l_ctr += 1
        if v == 'R':
            r_ctr += 1
        if i % 2 != 0:
            if l_ctr == r_ctr:
                balStr_ctr += 1
                l_ctr = 0
                r_ctr = 0
    print(balStr_ctr)
    return balStr_ctr

s = "LLLLRRRR"
balancedStringSplit(s)