def canBeEqual(target, arr):
    target.sort()
    arr.sort()
    target_dict = {i: v for i, v in enumerate(target)}
    arr_dict = {i: v for i, v in enumerate(arr)}
    print(target_dict)
    print(arr_dict)
    if(target_dict == arr_dict):
        print(True)
    else:
        print(False)
target = [1,2,2,3]
arr = [1,2,2,3]
canBeEqual(target, arr)