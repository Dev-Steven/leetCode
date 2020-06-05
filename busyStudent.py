def busyStudent(startTime, endTime, queryTime):
    total = 0
    for i in range(len(startTime)):
        if startTime[i] <= queryTime <= endTime[i]:
            total += 1
    print(total)
    return total
startTime = [1,2,3]
endTime = [3,2,7]
queryTime = 4
busyStudent(startTime, endTime, queryTime)