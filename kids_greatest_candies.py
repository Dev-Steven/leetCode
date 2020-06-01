def kidsWithCandies(candies, extraCandies):
    greatest = 0
    arr = []

    for candy in candies:
        if candy > greatest:
            greatest = candy
    
    for candy in candies:
        if candy + extraCandies >= greatest:
            arr.append('apple')
        else:
            arr.append('pear')
    for fruit in arr:
        print(fruit)
    return arr

candies = [2,3,5,1,3]
extraCandies = 3
kidsWithCandies(candies, extraCandies)