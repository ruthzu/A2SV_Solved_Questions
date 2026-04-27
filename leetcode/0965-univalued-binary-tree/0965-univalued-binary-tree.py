# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        cval = root.val
        q= deque([root])
        # print(q)
        while q:
            node = q.popleft()

            if node.val != cval:
                return False
            
            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return True


        # def tran(node):
        #     if not node:
        #         return True
        #      if node.left and node.left.val != node.val:
        #         return False
        #     if node.right and node.right.val != node.val:
        #         return False
        #     return tran(node.left) and tran(node.right)

        # return tran(root)



