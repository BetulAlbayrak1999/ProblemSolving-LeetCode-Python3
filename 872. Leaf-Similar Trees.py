class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode)-> bool:
        def getLeaves(root: TreeNode):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            return getLeaves(root.left) + getLeaves(root.right)

        leaves1= getLeaves(root1)
        leaves2= getLeaves(root2)

        return leaves1== leaves2


root1= TreeNode (3)
root1.left= TreeNode(5, TreeNode(6), TreeNode(3, TreeNode(7), TreeNode(4)))
root1.right = TreeNode (1, None, TreeNode(9))

root2= TreeNode(5)
root2.left= TreeNode(6)
root2.right= TreeNode(1, TreeNode(2, TreeNode(7), TreeNode(4)), TreeNode(9))

solution =Solution ()
print(solution.leafSimiler(root1, root2))