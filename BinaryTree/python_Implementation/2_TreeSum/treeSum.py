# Think about the base case -> Null node in this case will return 0, how the parent can compute its result given its left and right answers
# Bottom Up
class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def DFS(root):
    # base case :
    if root == None:
        return 0

    # Go left
    leftSum = DFS(root.left) # 4
    # Go Right
    rightSum = DFS(root.right) # -2

    # 11 + 4 + -2 = 13
    return root.val + leftSum + rightSum

def treeSum(root):

    return DFS(root)

if __name__ == "__main__":
    # //       3
    # //    /    \
    # //   11     4
    # //  / \      \
    # // 4   -2     1
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(-2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    print(f"The tree sum of this binary tree is {treeSum(a)}")