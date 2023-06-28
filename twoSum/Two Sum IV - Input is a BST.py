from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findTarget(root: TreeNode, k: int) -> bool:
    vals = {}

    def helper(root: TreeNode) -> bool:
        if root is None:
            return False
        if root.val in vals:
            return True
        vals[k - root.val] = True
        return helper(root.left) or helper(root.right)

    return helper(root)


# Test case
#       5
#      / \
#     3   6
#    / \   \
#   2   4   7

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

k = 9
result = findTarget(root, k)
print(result)  # Expected output: True
