class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    def backtracking(node, s):
        if node == None:
            return False
        s -= node.val
        if node.left == None and node.right == None:
            if s == 0:
                return True
        
        return backtracking(node.left, s) or backtracking(node.right, s)
    
    return backtracking(root, targetSum)
    

if __name__ == "__main__":
    root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    targetSum = 22

    treeNodes = [TreeNode(val=i) for i in root if i != None]

    treeNodes[0].left = treeNodes[1]
    treeNodes[0].right = treeNodes[2]

    treeNodes[1].left = treeNodes[3]

    treeNodes[2].left = treeNodes[4]
    treeNodes[2].right = treeNodes[5]

    treeNodes[5].right = treeNodes[8]

    treeNodes[3].left = treeNodes[6]
    treeNodes[3].right = treeNodes[7]

    print(f"Does a root-to-leaf path exist for the sum of {targetSum} ? {hasPathSum(treeNodes[0], targetSum)}")




