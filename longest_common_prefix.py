from typing import List


class Solution:
    def min_lenght(self, str1, str2):
        return len(str1) if len(str1) < len(str2) else len(str2)

    def common_prefix(self, str1, str2):
        min_len = self.min_lenght(str1, str2)
        str_list_1 = list(str1[:min_len])
        common = []
        for i in range(min_len):
            if str1[i] != str2[i]:
                common.append("")
            else:
                common.append("")
        return "".join(str_list_1)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1 or len(strs) > 200:
            return "Make sure 1 <= strs.length <= 200"
        if len(strs) == 1:
            return strs[0]
        common = self.common_prefix(strs[0], strs[1])
        if len(strs) == 2:
            return common
        for string in strs[2:]:
            common = self.common_prefix(common, string)
        return common


sol = Solution()
sol.longestCommonPrefix(["cir","car"])
