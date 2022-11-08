class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode) -> bool:
    # Idea : Recursive backtracking, we recursively explore the left and right subtrees of each root node.
    #        - 3 conditions to satisfy for a binary tree to be a mirror of itself :
    #           1) (the immediate children of the currently explore node) node.left.val == node.right.val 
    #           2) node.left.left == node.right.right (left child of the left subtree must be the same as the right child of the right subtree)
    #           3) node.left.right == node.right.left
    def isMirror(left, right):
        # Empty left and right tree are always a valid mirror
        if left == None and right == None:
            return True
        # either left ot right are not empty are an invalid mirror
        if left == None or right == None:
            return False
        
        # 1) & 2) & 3)
        return left.val == right.val and isMirror(left.left,right.right) and isMirror(left.right,right.left)
    
    return isMirror(root.left,root.right)
   

root = [1,2,2,3,4,4,3]
treeNodes = [TreeNode(val=root[i]) for i in range(len(root)) if root[i] != None]

treeNodes[0].left = treeNodes[1]
treeNodes[0].right = treeNodes[2]

treeNodes[1].left = treeNodes[3]
treeNodes[1].right = treeNodes[4]

treeNodes[2].left = treeNodes[5]
treeNodes[2].right = treeNodes[6]

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
print(f"Is the binary tree represented by root 1 symmetric ? {isSymmetric(treeNodes[0])}")

root2 = [1,2,2,None,3,None,3]
treeNodes2 = [TreeNode(val=root2[i]) for i in range(len(root2)) if root2[i] != None]

treeNodes2[0].left = treeNodes2[1]
treeNodes2[0].right = treeNodes2[2]

treeNodes2[1].right = treeNodes2[3]

treeNodes2[2].right = treeNodes2[4]

#     1
#    / \
#   2   2
#    \   \
#     3   3
print(f"Is the binary tree represented by root 2 symmetric ? {isSymmetric(treeNodes2[0])}")

