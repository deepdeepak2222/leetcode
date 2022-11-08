class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 1 or len(s) > pow(10, 4):
            return False
        set_str = set(s)
        if len(set_str) > 6:
            return False
        possible_values = "()[]{}"
        for char in set_str:
            if char not in possible_values:
                return False
        bracket_map = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        stack = []
        for char in s:
            if char in bracket_map:
                # push
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if char != bracket_map.get(popped):
                    return False

        return not len(stack)


inputs = [
    "123",
    "()",
    ")",
    ")",
    "(",
    "{][]}",
    "{][]}[()",
    "(}",
    "([)]",
    "{[]}",
    "{[()]}",
    "{[)(]}",
]
solution = Solution()
for val in inputs:
    print("Input: ", val, "  and output: ", solution.isValid(val))