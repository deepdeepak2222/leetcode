class Solution:
    def removeDuplicates(self, nums):
        if not nums or len(nums) > (3 * pow(10, 4)):
            return 0
        k = 0
        list_with_unique_value = []
        for item in nums:
            if item not in list_with_unique_value:
                list_with_unique_value.append(item)
        for index, val in enumerate(list_with_unique_value):
            nums[index] = val
        return len(list_with_unique_value)


print(Solution().removeDuplicates([1,2,3,4,4,5]))

# Better algorithm
"""
replace_counter = 1
for index in range(1, len(input_array)):
    if input_array[index-1] != input_array[index]:
        input_array[replace_counter] = input_array[index]
        replace_counter += 1
return replace_counter
"""