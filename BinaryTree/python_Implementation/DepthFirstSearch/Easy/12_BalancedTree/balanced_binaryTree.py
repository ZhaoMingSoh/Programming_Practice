class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: TreeNode) -> bool:
    def DFS_Recur(node):
        # Empty Tree is always True
        if node == None:
            return True, 0 # this 0 returns will not mess with the calculation and ensuring it is valid for all the parent trees

        b_balancedLeft, leftHeight = DFS_Recur(node.left)
        # If left subtree is found to be not balanced, immediately return False and terminate the recursion
        if not b_balancedLeft:
            return False, 0
        b_balancedRight, rightHeight = DFS_Recur(node.right)
        # If right subtree is found to be not balanced, immediately return False and terminate the recursion
        if not b_balancedRight:
            return False, 0
        
        # Check if the current subtree is balanced or not by checking its absolute difference, return the max height of either left or right subtrees
        return abs(leftHeight-rightHeight) <= 1, max(leftHeight,rightHeight) + 1

    b_Balanced = DFS_Recur(root)[0]
    return b_Balanced

root = [3,9,20,None,None,15,7]

treeNodes = [TreeNode(val=root[i]) for i in range(len(root)) if root[i] != None]

treeNodes[0].left = treeNodes[1]
treeNodes[0].right = treeNodes[2]

treeNodes[2].left = treeNodes[3]
treeNodes[2].right = treeNodes[4]

#     3
#    / \
#   9   20
#       / \
#      15  7

print(f"Is the binary tree represented by root 1 balanced ? {isBalanced(treeNodes[0])}")