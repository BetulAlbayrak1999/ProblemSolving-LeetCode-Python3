# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:
        if not root:
            return
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def print_tree(self, root):
        if not root:
            return
        queue = [root]
        while queue:
            current = queue.pop(0)
            print(current.val, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(7, TreeNode(6), TreeNode(9))

solution = Solution()
inverted_tree = solution.invertTree(root)
solution.print_tree(inverted_tree)
