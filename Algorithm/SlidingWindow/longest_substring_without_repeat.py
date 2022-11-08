"""
3. Longest Substring Without Repeating Characters
Medium

30029

1280

Add to List

Share
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


def get_window(win_start, win_end, len_string, window_size):
    if win_start == win_end == -1:
        win_start = 0
        win_end = win_start + window_size
    else:
        if win_start + 1 >= len_string and window_size > 1:
            window_size = window_size - 1
            win_start = 0
            win_end = win_start + window_size
        else:
            win_start = win_start + 1
            win_end = win_end + 1

    return win_start, win_end, window_size


def longest_substring_without_repeat_chars(input_string):
    if not input_string:
        return ""
    longest_substring = ""
    len_string = len(input_string)
    window_size = len(input_string)
    win_start = -1
    win_end = -1

    while True:
        win_start, win_end, window_size = get_window(win_start, win_end, len_string, window_size)
        print(win_start, win_end, window_size)
        window = input_string[win_start:win_end]
        if len(set(window)) == len(window):
            # No repeat chars in this window
            longest_substring = window if len(window) > len(longest_substring) else longest_substring
        if window_size == 1 and win_start >= len_string:
            break
    print(longest_substring)
    return longest_substring


# longest_substring_without_repeat_chars("abcabcbb")
# longest_substring_without_repeat_chars("bbbbb")
# longest_substring_without_repeat_chars("pwwkew")
# longest_substring_without_repeat_chars("b")
# longest_substring_without_repeat_chars("")
# longest_substring_without_repeat_chars("abcabcbb")
# longest_substring_without_repeat_chars("aab")

"""
    Optimised solution.
    
    Runtime: 1553 ms, faster than 8.11% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.2 MB, less than 13.78% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""
from collections import OrderedDict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        len_s = len(s)
        max_substring = ""
        for i in range(len_s):
            window = OrderedDict()
            window[s[i]] = 1
            window_start = i + 1
            while window_start < len_s:
                if not window.get(s[window_start]):
                    window[s[window_start]] = 1
                    window_start += 1
                else:
                    break
            tmp_substring = "".join(window.keys())
            max_substring = tmp_substring if len(tmp_substring) > len(max_substring) else max_substring
        print(max_substring)
        return max_substring


Solution().lengthOfLongestSubstring("abcabcbb")
Solution().lengthOfLongestSubstring("bbbbb")
Solution().lengthOfLongestSubstring("pwwkew")
Solution().lengthOfLongestSubstring("b")
Solution().lengthOfLongestSubstring("")
# longest_substring_without_repeat_chars("abcabcbb")
Solution().lengthOfLongestSubstring("aab")