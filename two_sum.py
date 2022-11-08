"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2 or len(nums) > 10000:
            return "Plz check. 2 <= nums.length <= 104"
        val_limit = 1000000000
        if target < -val_limit or target > val_limit:
            return "Plz check. -109 <= target <= 109"

        val_indexes_map = {}
        for i in range(len(nums)):
            if nums[i] < -val_limit or nums[i] > val_limit:
                return "Plz check. -109 <= nums[i] <= 109"
            num_0 = nums[i]
            req_num_1 = target - num_0
            if req_num_1 in val_indexes_map:
                # same number can also be the one
                return [i, val_indexes_map[req_num_1]]
            else:
                # add that with index in map
                val_indexes_map[nums[i]] = i
        # Not found
        return []
