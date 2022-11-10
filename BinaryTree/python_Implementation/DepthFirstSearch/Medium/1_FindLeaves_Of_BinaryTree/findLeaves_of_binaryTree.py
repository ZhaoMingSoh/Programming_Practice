class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findLeaves(root: TreeNode) -> list[list[int]]:
    collectLeafNodes = []
    # Bottom Up Approach :
    def DFS_Recur(node):
        # Null Node
        if node == None:
            return 0

        # PreOrder traversal : L -> R -> N
        leftHeight = DFS_Recur(node.left)
        rightHeight = DFS_Recur(node.right)

        # To determine the height of the current node, find the max(left child, right child) height
        # We're gonna use the height to determine if the array is of the right size
        if len(collectLeafNodes) < max(leftHeight,rightHeight)+1:
            # If not, we're gonna extend it, so that we can store the val at the position via height
            collectLeafNodes.extend([[]])
        
        # If yes, simply store it in the right position
        collectLeafNodes[max(leftHeight,rightHeight)].append(node.val)

        # Increment the current node height's by 1 and return
        return 1 + max(leftHeight,rightHeight)

    DFS_Recur(root)
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