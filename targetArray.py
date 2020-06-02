def createTargetArray(nums, index):
    targetArr = []
    for i in range(len(index)):
        targetArr.insert(index[i], nums[i])
    print(targetArr)
    return targetArr

nums = [0,1,2,3,4]
index = [0,1,2,2,1]
createTargetArray(nums, index)