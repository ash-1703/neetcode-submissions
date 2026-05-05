# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        recursive approach
        base case: if tree is empty - return None
        recursive step: invert the tree by recursively calling the funciton of 
        left and right children
        swap the left and right children of current node
        return root node


        if root is None, return None
        recursively invert the left and right subtrees
        swap left and right children
        return root node
        """

        # if not root:
        #     return None

        # left_inverted = self.invertTree(root.left)
        # right_inverted = self.invertTree(root.right)

        # root.left, root.right = right_inverted, left_inverted

        # return root

        """
        iteratively
        """
        if not root:
            return None
        
        queue = deque([root])

        while queue:
            node = queue.popleft()

            node.left,node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
