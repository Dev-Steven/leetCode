def decompressRLElist(nums):
    arr = []
    freq=0
    val=0
    for i, v in enumerate(nums):
        # freq is always 0, 2 indexes. Assign frequency
        if i%2 == 0:
            freq = v
        # assign v to val and use for loop to add the val to arr freq amount of times
        else:
            val = v
            for x in range(freq):
                arr.append(val)
    print(arr)
    return arr

nums = [1,2,3,4]
decompressRLElist(nums)