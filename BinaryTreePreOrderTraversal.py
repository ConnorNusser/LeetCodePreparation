# https://leetcode.com/problems/binary-tree-preorder-traversal/
class Solution:
    def __init__(self):
        self.return_list=[]
            
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        self.return_list.append(root.val)
        
        self.preorderTraversal(root.left)
        
        self.preorderTraversal(root.right)
        
        return self.return_list