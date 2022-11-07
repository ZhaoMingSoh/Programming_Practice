class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root: TreeNode, low: int, high: int) -> int:
        # Inorder Recursive DFS - bottom up approach
        def DFS(node, low, high):
            sum_ = 0
            # The base case of when a node is Null -> return 0 so it doesn't affect the rangesum
            if node == None:
                return 0
            
            sum_ += DFS(node.left, low, high) # The range sum from the left child
            # Add the current node val into the current sum if and only if it is in the range [low,high]
            if node.val >= low and node.val <= high:
                sum_ += node.val
            sum_ += DFS(node.right, low, high) # The range sum from the right child
            
            return sum_
        
        return DFS(root, low, high)

if __name__ == "__main__":
    #          10
    #        /    \
    #       5      15
    #      / \     / \
    #     3   7   13  18
    #    /   /
    #   1   6
    root = [10,5,15,3,7,13,18,1,None,6]
    treeNodes = [TreeNode(val=root[i]) for i in range(len(root)) if root[i] != None]
    # Build the binary tree   
    treeNodes[0].left = treeNodes[1]
    treeNodes[0].right = treeNodes[2]

    treeNodes[1].left = treeNodes[3]
    treeNodes[1].right = treeNodes[4]

    treeNodes[2].left = treeNodes[5]
    treeNodes[2].right = treeNodes[6]

    treeNodes[3].left = treeNodes[7]

    treeNodes[4].left = treeNodes[8]

    low = 6
    high = 10

    print(f"The sum of all values between [{low},{high}] is {rangeSumBST(treeNodes[0], low, high)}")

    

