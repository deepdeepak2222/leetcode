"""
7. Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0). Go to the editor
Test Data:
sum_series(6) -> 12
sum_series(10) -> 30
"""


def sum_series_func(num, sum_series=0):
    if num < 0:
        return sum_series
    sum_series = sum_series + num
    return sum_series_func(num - 2, sum_series)


print("sum_series(6) -> 12: ", sum_series_func(6))
print("sum_series(10) -> 30: ", sum_series_func(10))
