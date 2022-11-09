class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def findLeaves(root: TreeNode) -> list[list[int]]:
    collectLeafNodes = []
    while(root != None):
        leafNodes = []
        if root.left == None and root.right == None:
            leafNodes.append(root.val)
            collectLeafNodes.append(leafNodes)
            break

        def DFS_Recur(node, leafNodes):
            print(node.val)
            # Leaf node
            if node.left == None and node.right == None:
                leafNodes.append(node.val)
                return
                
            # Delete the leaf node by setting its parent's either left or right branch to point to None
            DFS_Recur(node.left,leafNodes)
            node.left = None
            DFS_Recur(node.right,leafNodes)
            node.right = None

            return
        DFS_Recur(root, leafNodes)
        print(leafNodes)
        collectLeafNodes.append(leafNodes)

    return collectLeafNodes

if __name__ == "__main__":
    root = [1,2,3,4,5]
    treeNodes = [TreeNode(val=i) for i in root if i != None]

    # Build binary tree from given root
    treeNodes[0].left = treeNodes[1]
    treeNodes[0].right = treeNodes[2]

    treeNodes[1].left = treeNodes[3]
    treeNodes[1].right = treeNodes[4]

    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5

    print(f"All leaves nodes in the binary Tree in order: {findLeaves(treeNodes[0])}")
    root2 = [1]
    treeNodes2 = [TreeNode(val=i) for i in root2 if i != None]
