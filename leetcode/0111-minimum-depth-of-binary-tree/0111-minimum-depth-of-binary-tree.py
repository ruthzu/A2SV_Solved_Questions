# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]):
        def mindepth(root):
            if not root:
                return 0
            if not root.left:
                return 1 + mindepth(root.right)
            if not root.right:
                return 1 + mindepth(root.left)

            return 1 + min(mindepth(root.left), mindepth(root.right))
        return mindepth(root)