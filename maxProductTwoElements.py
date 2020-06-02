def maxProduct(nums):
    max_1 = 0
    max_2 = 0
    indexTaken = 0
    product = 0
    if len(nums) == 2:
        product = (nums[0] - 1) * (nums[1] -1)
        print(product)
        return product
    # find max_1
    for i, num in enumerate(nums):
        if num > max_1:
            max_1 = num
            indexTaken = i
    # find max_2
    for i, num in enumerate(nums):
        if num > max_2 and i != indexTaken:
            max_2 = num
    product = (max_1 - 1) * (max_2 -1)
    print(product)
    return product

nums = [3,4,5,2]
maxProduct(nums)