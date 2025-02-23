# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    preInd = 0
    postInd = 0
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        node = TreeNode(preorder[self.preInd])
        self.preInd += 1

        if node.val != postorder[self.postInd]:
            node.left = self.constructFromPrePost(preorder, postorder)
        if node.val != postorder[self.postInd]:
            node.right = self.constructFromPrePost(preorder, postorder)
        
        self.postInd += 1

        return node
