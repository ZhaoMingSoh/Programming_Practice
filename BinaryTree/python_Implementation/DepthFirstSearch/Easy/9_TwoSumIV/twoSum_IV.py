class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Top-down approach : DFS Recursion
def findTarget(root : TreeNode, k) -> bool:
    hashSet = set()

    def DFS_Recur(node, hashSet, target):
        if node == None:
            return
        # If we find the target - node.val in the hashSet, this means the x + y = target (y has been found)
        if target - node.val in hashSet:
            return True
        
        hashSet.add(node.val)

        if DFS_Recur(node.left,hashSet,target):
            return True
        if DFS_Recur(node.right,hashSet,target):
            return True

        # After going through the left and right subtree and no match was found in the hashSet
        return False

    return DFS_Recur(root, hashSet, k)

if __name__ == "__main__":
    root = [5,3,6,2,4,None,7]
    treeNodes = [TreeNode(val=root[i]) for i in range(len(root)) if root[i] != None]
    # Build the binary tree   
    treeNodes[0].left = treeNodes[1]
    treeNodes[0].right = treeNodes[2]

    treeNodes[1].left = treeNodes[3]
    treeNodes[1].right = treeNodes[4]

    treeNodes[2].right = treeNodes[5]


    #         5
    #       /  \
    #      3    6
    #     / \    \
    #    2  4     7

    print(f"Can the sum of {9} be found in the binary tree represented by root 1 ? {findTarget(treeNodes[0], 9)}")
    print()