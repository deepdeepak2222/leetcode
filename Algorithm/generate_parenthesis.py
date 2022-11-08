"""
    22. Generate Parentheses
    Medium

    15234

    580

    Add to List

    Share
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



    Example 1:

    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
    Example 2:

    Input: n = 1
    Output: ["()"]


    Constraints:

    1 <= n <= 8

"""
from itertools import combinations, permutations


class Solution:
    def valid_combination(self, perm):
        stack = []
        for chr in perm:
            if chr == "(":
                stack.append(chr)
            else:
                if not stack:
                    return False
                stack.pop()
        return True

    def reverse_list(self, list_objs):
        char_map = {
            "(": ")",
            ")": "("
        }
        reversed_list = [char_map.get(chr) for chr in list_objs[::-1]]
        print("\n*** list_objs: ", list_objs, "    reversed_list: ", reversed_list)
        return reversed_list

    def generateParenthesis(self, n):
        import pdb
        pdb.set_trace()
        if n < 1 or n > 8:
            return []
        return_list = []
        for comb in combinations(["(", ")"], n - 1):
            comb = ("(", *comb)
            if "".join(comb) not in return_list and self.valid_combination(comb):
                perfect_parenthesis = list(comb)
                perfect_parenthesis.extend(self.reverse_list(perfect_parenthesis))
                return_list.append("".join(perfect_parenthesis))
        print("Input is ", n, " and return_list: ", return_list)
        return return_list


Solution().generateParenthesis(3)
# Solution().reverse_list(("(", "(", "("))








class SolutionOnLeetCode(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans