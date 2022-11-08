# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        left_to_right = True
        q = []
        return_list = []
        q.append(root)
        while len(q):
            number_of_current_level_nodes = len(q)
            current_level_values = []
            for i in range(0, number_of_current_level_nodes):
                popped_node = q.pop(0)
                current_level_values.append(popped_node.val)
                if popped_node.left:
                    q.append(popped_node.left)
                if popped_node.right:
                    q.append(popped_node.right)

            return_list.append(current_level_values) if left_to_right else return_list.append(
                current_level_values[::-1])
            left_to_right = not left_to_right
        return return_list
