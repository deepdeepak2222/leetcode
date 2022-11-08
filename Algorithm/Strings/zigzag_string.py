"""
    6. Zigzag Conversion
Medium

4495

9892

Add to List

Share
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"


Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000








Success
Details
Runtime: 116 ms, faster than 53.68% of Python3 online submissions for Zigzag Conversion.
Memory Usage: 14.2 MB, less than 13.98% of Python3 online submissions for Zigzag Conversion.
Next challenges:
Restore IP Addresses
Defanging an IP Address
Simplified Fractions

"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        s_len = len(s)
        out_arr = []
        for row in range(numRows):
            out_arr.append([])
        chr_index = 0
        while chr_index < s_len:
            tmp_str = s[chr_index:chr_index+numRows]
            for index, item in enumerate(tmp_str):
                out_arr[index].append(item)
            chr_index = chr_index + len(tmp_str)
            intermediate_chars = self.intermediate_chars(chr_index, s, out_arr, numRows)
            chr_index = chr_index + intermediate_chars
        ret_str = ""
        for items in out_arr:
            ret_str += "".join(items)
        return ret_str

    def intermediate_chars(self, chr_index, s, out_arr, numRows):
        total_chars = 0 if numRows <= 2 else (numRows-2)
        tmp = s[chr_index:chr_index+total_chars]
        for i, item in enumerate(tmp):
            out_arr[numRows-i-2].append(item)
        return len(tmp)


assert "PAHNAPLSIIGYIR" == Solution().convert("PAYPALISHIRING", 3)
assert "PINALSIGYAHRPI" == Solution().convert("PAYPALISHIRING", 4)
assert "PAYPALISHIRING" == Solution().convert("PAYPALISHIRING", 1)
enumerate()