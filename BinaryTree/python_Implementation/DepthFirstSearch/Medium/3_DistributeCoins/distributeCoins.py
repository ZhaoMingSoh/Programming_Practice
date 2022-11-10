class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def distributeCoins( root: TreeNode) -> int:
    ans = 0

    def dfs(node):
        nonlocal ans
        if node == None: return 0
        # number of coins in need from parent (-) or in extra to parent (+)
        L = dfs(node.left)
        R = dfs(node.right)
        # the number of coins in excess is exactly the minimum number of coins required to make every node have exactly 1 coin
        ans += abs(L) + abs(R)
        # the -1 is to make sure that the current node has exactly 1 coin and the rest are pass on or in need
        return node.val + L + R - 1

    dfs(root)

    return ans
        

if __name__ == "__main__":
    root = [3,0,0]
    treeNodes = [TreeNode(i) for i in root if i != None]

    treeNodes[0].left = treeNodes[1]
    treeNodes[0].right = treeNodes[2]
    
    #     3
    #    / \
    #   0   0

    print(f"Minimum number of moves required for every node to have exactly one coin in root 1 is {distributeCoins(treeNodes[0])}")
    root2 = [0,3,0]
    treeNodes2 = [TreeNode(i) for i in root2 if i != None]

    treeNodes2[0].left = treeNodes2[1]
    treeNodes2[0].right = treeNodes2[2]
    
    #     0
    #    / \
    #   3   0

    print(f"Minimum number of moves required for every node to have exactly one coin in root 2 is {distributeCoins(treeNodes2[0])}")
