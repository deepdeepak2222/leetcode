from typing import List


def sum_list(arr: List, sum_all=0):
    if len(arr) > 0:
        if isinstance(arr[0], list):
            return sum_list([*arr[0], *arr[1:]], sum_all)
        sum_all = sum_all + arr[0]
    else:
        return sum_all
    return sum_list(arr[1:], sum_all)


sum_list([1, 2, [3, 4], [5, 6]])
sum_list([1, 2, [3, 4], [5, 6], [3, 4, 5, [1, 2, [2, 1]]]])   #39
