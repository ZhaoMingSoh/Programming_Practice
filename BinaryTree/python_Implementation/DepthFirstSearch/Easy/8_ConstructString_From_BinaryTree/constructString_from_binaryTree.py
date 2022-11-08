class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def PreOrder(node, result):
    if node == None:
        return
    result.append(str(node.val))
    # 1) If the left child exist, add the braces to the left child
    if node.left != None:
        result.append('(')
        PreOrder(node.left, result)
        result.append(')')
    # 3) If only left child exist, we can omit the right child braces as it will not mess with the 1-to-1 mapping of the string with the binary tree

    # 1) If the right child exist, add the braces to the right child
    if node.right != None:
        # 4) If only the right child exist, we have to add in the braces for the left because it is always considered before the right in the PreOrder traversal
        if node.left == None:
            result.append("()")
        result.append('(')
        PreOrder(node.right, result)
        result.append(')')

    return

def tree2str(root: TreeNode) -> str:
    result = []
    PreOrder(root, result)
    return ''.join(result)

if __name__ == "__main__":
    root = [1,2,3,4]
    treeNodes = [TreeNode(val=root[i]) for i in range(len(root)) if root[i] != None]
    # Build the binary tree   
    treeNodes[0].left = treeNodes[1]
    treeNodes[0].right = treeNodes[2]

    treeNodes[1].left = treeNodes[3]

    #         1
    #       /  \
    #      2    3
    #     /
    #    4

    print(f"What is the string that can be constructed by binary tree 1 ? {tree2str(treeNodes[0])}")
    print()

    root2 = [1,2,3,None,4]
    treeNodes2 = [TreeNode(val=root2[i]) for i in range(len(root2)) if root2[i] != None]

    treeNodes2[0].left = treeNodes2[1]
    treeNodes2[0].right = treeNodes2[2]
    
    treeNodes2[1].left = None
    treeNodes2[1].right  = treeNodes2[3]

    print(f"What is the string that can be constructed by binary tree 2 ? {tree2str(treeNodes2[0])}")
    print()
