# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1,leaf2 = [], []
        self.getLeafDFS(root1,leaf1)
        self.getLeafDFS(root2,leaf2)
        return leaf1 == leaf2
    
    def getLeafDFS(self,node,res):
        if not node:
            return
        self.getLeafDFS(node.left,res)
        self.getLeafDFS(node.right,res)
        if (not node.left) and (not node.right):
            res.append(node.val)
