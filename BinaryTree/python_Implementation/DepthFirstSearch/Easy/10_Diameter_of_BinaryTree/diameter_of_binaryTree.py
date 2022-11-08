import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Bottom Up Approach : The longest path must be between leaf to leaf nodes.
#                       - recursively explore the entire tree rooted at the given node, find the longest path from its left and right children.
#                       - if left + right > diameter, replace it by left + right which indicate a new longest path.
#                       - return the longest of the 2 children + 1 (indicate an edge between the children and its parent root node) 
def diameterOfBinaryTree(root: TreeNode) -> int:
    longestPath = -(math.inf)
    
    def DFS_Recur(node):
        nonlocal longestPath
        if node == None:
            return 0
        
        leftPath = DFS_Recur(node.left)
        rightPath = DFS_Recur(node.right)
        
        longestPath = max(longestPath, leftPath + rightPath)
        return max(leftPath,rightPath) + 1
    DFS_Recur(root)
    return longestPath

if __name__ == "__main__":
    root = [1,2,3,4,5]
    treeNodes = [TreeNode(val=root[i]) for i in range(len(root)) if root[i] != None]

    treeNodes[0].left = treeNodes[1]
    treeNodes[0].right = treeNodes[2]

    treeNodes[1].left = treeNodes[3]
    treeNodes[1].right = treeNodes[4]

    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    print(f"The longest path from leaf to leaf node is {diameterOfBinaryTree(treeNodes[0])}")

    root2 = [1,2]
    treeNodes2 = [TreeNode(val=root2[i]) for i in range(len(root2)) if root2[i] != None]

    treeNodes2[0].left = treeNodes2[1]

    #      1
    #     /
    #    2 
    print(f"The longest path from leaf to leaf node is {diameterOfBinaryTree(treeNodes2[0])}")
