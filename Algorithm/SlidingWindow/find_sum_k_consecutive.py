def find_sum_of_k_consecutive(num_arr, k):
    len_arr = len(num_arr)

    if len_arr < k:
        return -1
    window_start = 0
    window_end = window_start + k
    max_sum = 0
    while window_start < len_arr:
        if len(num_arr[window_start: window_end]) < k:
            break
        max_sum = max(max_sum, sum(num_arr[window_start: window_end]))
        window_start = window_start + 1
        window_end = window_end + 1

    print(max_sum)
    return max_sum


assert find_sum_of_k_consecutive([100, 200, 300, 400], 2) == 700
assert find_sum_of_k_consecutive([1, 4, 2, 10, 2, 3, 1, 0, 20], 4) == 24
