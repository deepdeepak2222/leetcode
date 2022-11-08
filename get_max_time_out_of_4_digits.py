"""
Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

Return the latest 24-hour time in "HH:MM" format. If no valid time can be made, return an empty string.



Example 1:

Input: arr = [1,2,3,4]
Output: "23:41"
Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.
Example 2:

Input: arr = [5,5,5,5]
Output: ""
Explanation: There are no valid 24-hour times as "55:55" is not valid.


Constraints:

arr.length == 4
0 <= arr[i] <= 9

"""
from typing import List


class TimeObj:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute


class Solution:
    def get_bigger_time(self, time_1: TimeObj, time_2: TimeObj):
        if time_1.hour > time_2.hour:
            return time_1
        elif time_1.hour < time_2.hour:
            return time_2
        else:  # if hour is equal
            return time_1 if time_1.minute > time_2.minute else time_2

    def return_time_str(self, time_obj: TimeObj):
        hour = str(time_obj.hour) if len(str(time_obj.hour)) == 2 else "0%s" % str(time_obj.hour)
        minute = str(time_obj.minute) if len(str(time_obj.minute)) == 2 else "0%s" % str(time_obj.minute)
        return "%s:%s" % (hour, minute)

    def largestTimeFromDigits(self, arr: List[int]) -> str:
        if len(arr) != 4:
            return ""

        max_time = TimeObj(0, 0)
        found = False
        for i in range(0, 4):
            for j in range(0, 4):
                for k in range(0, 4):
                    for l in range(0, 4):
                        if arr[i] > 2:
                            continue
                        if len(set((i, j, k, l))) == 4:
                            # hour consists i and j
                            time_hour = arr[i] * 10 + arr[j]
                            if time_hour > 23:
                                continue
                            time_min = arr[k] * 10 + arr[l]
                            if time_min > 59:
                                continue
                            found = True
                            max_time = self.get_bigger_time(max_time, TimeObj(time_hour, time_min))

        if not found:
            return ""

        if max_time.hour == 0 and max_time.minute == 0:
            set_arr = set(arr)
            if 0 not in set_arr:
                return ""

        return self.return_time_str(max_time)


print(Solution().largestTimeFromDigits([9, 0, 7, 7]))

if __name__ == "main":
    print(Solution().largestTimeFromDigits([9, 0, 7, 7]))
    print("\n*** Hello")
