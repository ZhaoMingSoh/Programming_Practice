class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# One step right and then always left
def successor( root: TreeNode) -> int:
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
# One step left and then always right
def predecessor( root: TreeNode) -> int:
    root = root.left
    while root.right:
        root = root.right
    return root.val

def deleteNode( root: TreeNode, key: int) -> TreeNode:
    if not root:
        return None

    # delete from the right subtree
    if key > root.val:
        root.right = deleteNode(root.right, key)
    # delete from the left subtree
    elif key < root.val:
        root.left = deleteNode(root.left, key)
    # delete the current node
    else:
        # the node is a leaf
        if not (root.left or root.right):
            root = None
        # the node is not a leaf and has a right child
        elif root.right:
            root.val = successor(root)
            root.right = deleteNode(root.right, root.val)
        # the node is not a leaf, has no right child, and has a left child    
        else:
            root.val = predecessor(root)
            root.left = deleteNode(root.left, root.val)
                    
    return root

def dfs_In(node):
    if not node:
        return
    
    print(node.val, end=" ")
    dfs_In(node.left)
    dfs_In(node.right)

    return

if __name__ == "__main__":
    root1 = [2,1,33,None,None,25,40,11,None,34,None,7,12,None,36,None,None,None,13]
    # [2,1,33,25,40,11,34,7,12,36,13]
    treeNodes1 = [TreeNode(i) for i in root1 if i != None]

    # 2
    treeNodes1[0].left = treeNodes1[1]
    treeNodes1[0].right = treeNodes1[2]
    
    # 33
    treeNodes1[2].left = treeNodes1[3]
    treeNodes1[2].right = treeNodes1[4]

    # 25
    treeNodes1[3].left = treeNodes1[5]

    # 40
    treeNodes1[4].left = treeNodes1[6]

    # 11
    treeNodes1[5].left = treeNodes1[7]
    treeNodes1[5].right = treeNodes1[8]

    # 34
    treeNodes1[6].right = treeNodes1[9]

    # 12
    treeNodes1[7].right = treeNodes1[10]

    deleteNode(treeNodes1[0], 33)
    dfs_In(treeNodes1[0])
    