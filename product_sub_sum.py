def subtractProductAndSum(theInt):
    # convert to string to iterate
    intToString = str(theInt)
    # create produt and sum
    totalProduct = 1
    totalSum = 0
    # iterate through string
    for digit in intToString:
        totalProduct = int(float(digit)) * totalProduct
    for digit in intToString:
        totalSum = int(digit) + totalSum
    return totalProduct - totalSum

theInt = 123
subtractProductAndSum(theInt)
