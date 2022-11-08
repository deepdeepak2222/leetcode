def factorial(num, fact=1):
    if num < 1:
        return -1
    if num == 1:
        return fact
    fact = fact * num
    return factorial(num-1, fact)


factorial(3)
