# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def f(n, p, g):
            if not n:
                return 0
            s = 0
            if g and g % 2 == 0:
                s += n.val
            s += f(n.left, n.val, p)
            s += f(n.right, n.val, p)
            return s
        return f(root, None, None)