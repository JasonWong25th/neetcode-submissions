# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #quick review
        #pre order is root, left, right
        #in order is left, root, right

        #key insight is that they both start with root / left

        #First instinct
        #since I know the root is always going to be on the left
        #and inorder is going to be in the center
        #I want to break this problem into sub problems
        #finding the sub arrays for the right and left trees
        inorder_index = {value:index for index, value in enumerate(inorder)}
        pre_root_index = 0
        def helper(left, right):
            nonlocal pre_root_index
            if left > right:
                return None

            root_val = preorder[pre_root_index]
            root_index = inorder_index[root_val]
            pre_root_index+=1

            tree = TreeNode(root_val)
            tree.left = helper(left, root_index-1)
            tree.right = helper(root_index+1, right)
            return tree
        return helper(0, len(inorder)-1)




        