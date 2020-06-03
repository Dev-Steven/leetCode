def minCostToMoveChips(chips):
    odd_chip = 0
    even_chip = 0
    # even chips can be changed to same value for free by adding 2
    # odd chips can be changed to same value for free by adding 2 
    # moving chip by 2 costs 0
    # Basically this means ALL even chips can be treated the same AND
    # ALL odd chips can be treated the same
    # [1,2,3,4,5] -> [1,2,1,2,1]
    # add 1 because the cost of changing the value to either even or odd is 1
    for chip in chips:
        if chip % 2 == 0:
            even_chip += 1
        else:
            odd_chip += 1
    # find who is the smallest - odd or even 
    # then change that number for min cost 
    # BASICALLY return the total of even or odd depending on who is smaller
    # [1,2,1,2,1] -> [1,1,1,1,1]
    print(min(even_chip, odd_chip))
    return min(even_chip, odd_chip)
chips=[2,2,2,3,3]
minCostToMoveChips(chips)