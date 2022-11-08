def get_window(win_start, win_end, len_string, window_size):
    if win_start == win_end == -1:
        win_start = 0
        win_end = win_start + window_size
    else:
        if win_end + 1 >= len_string and window_size > 1:
            window_size = window_size - 1
            win_start = 0
            win_end = win_start + window_size
        else:
            win_start = win_start + 1
            win_end = win_end + 1

    return win_start, win_end, window_size


def longest_substring_without_repeat_chars(input_string):
    if not input_string:
        return 1
    longest_substring = ""
    len_string = len(input_string)
    window_size = len(input_string)
    win_start = -1
    win_end = -1

    while True:
        win_start, win_end, window_size = get_window(win_start, win_end, len_string, window_size)
        window = input_string[win_start:win_end]
        if len(set(window)) == len(window):
            # No repeat chars in this window
            longest_substring = window if len(window) > len(longest_substring) else longest_substring
        if window_size == 1 and win_start >= len_string:
            break

    return len(longest_substring)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return longest_substring_without_repeat_chars(s)
