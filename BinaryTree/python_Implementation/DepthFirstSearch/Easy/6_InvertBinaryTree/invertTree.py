import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Bottom Up approach : (Recursive)
def invertTree(root: TreeNode) -> TreeNode:
    # Just return the Null node as they will be swapped anyway with error
    if root == None:
        return root
    
    invertTree(root.left)
    invertTree(root.right)
    
    #Swap left and right subtree
    temp = root.left
    root.left = root.right
    root.right = temp
    
    return root

# Use Stack :
def invertTree_Iterative(root : TreeNode) -> TreeNode :
    # DFS
    if root == None:
        return root
    
    stack = collections.deque([root])
    
    while len(stack) != 0:
        cur_node = stack.popleft()
        
        # Swap the left and right children - starting from the top -> bot
        temp = cur_node.left
        cur_node.left = cur_node.right
        cur_node.right = temp
        
        if cur_node.left != None:
            stack.appendleft(cur_node.left)
        if cur_node.right != None:
            stack.appendleft(cur_node.right)
    
    return root

if __name__ == "__main__":
    root = [4,2,7,1,3,6,9]
    treeNodes = [TreeNode(val=root[i]) for i in range(len(root)) if root[i] != None]
    # Build the binary tree   
    treeNodes[0].left = treeNodes[1]
    treeNodes[0].right = treeNodes[2]

    treeNodes[1].left = treeNodes[3]
    treeNodes[1].right = treeNodes[4]

    treeNodes[2].left = treeNodes[5]
    treeNodes[2].right = treeNodes[6]

    #         4
    #       /   \
    #      2     7 
    #     / \   / \
    #    1   3 6   9

    print(f"The inverted tree :")
    invertTree(treeNodes[0])

    # Print the inverted binary tree
    def DFS(root):
        if root == None:
            return
        
        print(root.val, end=' ')
        DFS(root.left)
        DFS(root.right)

        return
    
    DFS(treeNodes[0])
    print()

