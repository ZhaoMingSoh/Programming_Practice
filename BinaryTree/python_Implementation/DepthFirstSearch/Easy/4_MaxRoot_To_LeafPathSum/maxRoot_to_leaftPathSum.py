import math
# Recursive approach - Bottom Up
# Base case -> check for leaf node (left and right are Null) and return the leaf node itself
#           -> if node -> null, return -infinity as it will not interfere with our comparison
# At each sub root node, we compare the sum of (root + left) to sum of (root + right), return the greater of the two
class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def DFS(node):
    if node == None:
        return -math.inf
    # Identify the leaf node
    if node.left == None and node.right == None:
        return node.val
    maxChildPathSum = max(DFS(node.left), DFS(node.right)) # choose the larger child path sum val
    return node.val + maxChildPathSum # return the sum of subroot + max child path sum val

def maxPathSum(root):
    # DFS -  Recursive Approach
    return DFS(root)

if __name__ == "__main__":
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(0)
    f = Node(-13)
    g = Node(-1)
    h = Node(-2)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    # //        -1
    # //      /   \
    # //    -6    -5
    # //   /  \     \
    # // -3   0    -13
    # //     /       \
    # //    -1       -2

    # a = Node(5)
    # b = Node(11)
    # c = Node(54)
    # d = Node(20)
    # e = Node(15)
    # f = Node(1)
    # g = Node(3)

    # a.left = b
    # a.right = c
    # b.left = d
    # b.right = e
    # e.left = f
    # e.right = g

# //        5
# //     /    \
# //    11    54
# //  /   \
# // 20   15
# //      / \
# //     1  3
    print(f"What is the max root to leaf path sum in this binary tree ? {maxPathSum(a)}")