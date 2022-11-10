class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Bottom Up Approach : DFS PreOrder because we're gonna prune the children first before the node itself
def pruneTree(root: TreeNode) -> TreeNode:
        def DFS_Recur(node):
            # Null Node
            if node == None:
                return False
            
            # PreOrder : L -> R -> N
            left = DFS_Recur(node.left)
            right = DFS_Recur(node.right)

            # Does the left child contain 1 ?
            if not left:
                node.left = None # Pruning
            # Does the right child contain 1 ?
            if not right:
                node.right = None # Pruning
            
            # If either node.val or left or right child has 1, then we cannot prune this node off
            if node.val == 1 or left or right:
                return True
            
            # If neither node.val or left or right child has 1
            return False
        
        if DFS_Recur(root):
            return root
    
        return None
        
def dfs(root):
        if root == None:
            return
        print(root.val, end=' ')
        dfs(root.left)
        dfs(root.right)

if __name__ == "__main__":
    root1 = [1,None,0,0,1]
    treeNodes = [TreeNode(val=i) for i in root1 if i != None]

    treeNodes[0].right = treeNodes[1]
    
    treeNodes[1].left = treeNodes[2]
    treeNodes[1].right = treeNodes[3]

    # 1
    #  \
    #   0
    #  / \
    # 0   1
    pruneTree(treeNodes[0])
    print(f"What does the root1 look like after pruning ? :")
    dfs(treeNodes[0])
    print()

    root2 = [1,0,1,0,0,0,1]
    treeNodes2 = [TreeNode(val=i) for i in root2 if i != None]
    root3 = [1,1,0,1,1,0,1,0]
    treeNodes3 = [TreeNode(val=i) for i in root3 if i != None]
