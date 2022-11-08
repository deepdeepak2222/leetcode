"""
    35. Search Insert Position
Easy

9821

472

Add to List

Share
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

"""
import math
from typing import List


class Solution:
    def binary_search(self, nums, start, end, target):
        mid_index = start + math.floor((end - start) / 2)

        if start == end and not target == nums[mid_index]:
            if target > nums[end]:
                return end + 1
            else:
                return start

        if target == nums[mid_index]:
            return mid_index
        elif target > nums[mid_index]:
            # call binary search on second half
            if (mid_index + 1) not in range(0, len(nums)):
                return mid_index
            return self.binary_search(nums, mid_index + 1, end, target)

        else:
            # call binary search on second half
            if (mid_index - 1) not in range(0, len(nums)):
                return mid_index
            return self.binary_search(nums, start, mid_index - 1, target)

    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) > 10000:
            return -1
        if target < -10000 or target > 10000:
            return -1
        index = self.binary_search(nums, 0, len(nums) - 1, target)

        return index


print(Solution().searchInsert([1, 3], 0))