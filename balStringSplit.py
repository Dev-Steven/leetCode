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
    # l_ctr = 0
    # r_ctr = 0
    # for i, v, in enumerate(s):
    #     if v == 'L':
    #         l_ctr += 1
    #     if v == 'R':
    #         r_ctr += 1
    #     if i % 2 != 0:
    #         if l_ctr == r_ctr:
    #             balStr_ctr += 1
    #             l_ctr = 0
    #             r_ctr = 0
    print(balStr_ctr)
    return balStr_ctr

s = "LLLLRRRR"
balancedStringSplit(s)