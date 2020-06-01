def decompressRLElist(nums):
    arr = []
    for i in range(0, len(nums), 2):
        freq = nums[i]
        val = nums[i+1]
        n = 0
        while n < freq:
            arr.append(val)
            n += 1
    for number in arr:
        print(number)
    return arr

nums = [1,2,3,4]
decompressRLElist(nums)