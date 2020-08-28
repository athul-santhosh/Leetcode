# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # self.count = 0
        # def preorder(start):
        #     if start:
        #         self.count += 1
        #         preorder(start.left)
        #         preorder(start.right)
        # preorder(root)
        # return self.count
        
        # use the advantage of complelte binary tree
        """
    1
   / \
  2   3
 / \  /
4  5 6
        if left pointer == right pointer:
            return 2 ** h - 1
        """
        if root is None:
            return 0
        
        leftcount = 0
        rightcount = 0
        left = root
        right = root
        while left:
            leftcount += 1
            left = left.left
        while right:
            rightcount += 1
            right = right.right
        if rightcount == leftcount:
            return 2**leftcount -1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        