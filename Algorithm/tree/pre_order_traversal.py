# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def getPreOrder(self, root):
        self.final_list.append(root.val)
        if root.left:
            self.getPreOrder(root.left)
        if root.right:
            self.getPreOrder(root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.final_list = []
        self.getPreOrder(root)
        return self.final_list
