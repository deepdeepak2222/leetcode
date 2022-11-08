# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = []
        queue.append(root)
        return_list = []
        while len(queue):
            current_level_values = []
            current_level_nodes = len(queue)
            for i in range(0, current_level_nodes):
                popped_node = queue.pop(0)
                current_level_values.append(popped_node.val)
                if popped_node.left:
                    queue.append(popped_node.left)
                if popped_node.right:
                    queue.append(popped_node.right)
            return_list.append(current_level_values)




