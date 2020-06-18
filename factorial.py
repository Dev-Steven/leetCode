def factorial(num):
    # base case
    if num < 2:
        return num
    else:
        return num * factorial(num - 1)

print(factorial(5))