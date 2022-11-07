import math
# Find the min value in the binary tree
# Base case -> Null return +infinity because it will not be taken in by the variable that keep tracks of the smallest value
# Bottom up approach :
#   we compare the parent value to its left and right childs value and keep the smallest

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def DFS(node):
    smallest_Value = math.inf # the norm is to initialise the smallest value with +infinity because then we can swap it with the first instance of comparison
    if node == None:
        return math.inf
    
    leftVal = DFS(node.left)
    rigthVal = DFS(node.right)

    # Find the smallest value in the left and righ subtree before comparing it to the root node of that subtree
    if leftVal < smallest_Value:
        smallest_Value = leftVal
    if rigthVal < smallest_Value:
        smallest_Value = rigthVal
    if node.val < smallest_Value:
        smallest_Value = node.val

    return smallest_Value

def treeMinValue(root):
    # DFS - Recursive Approach
    return DFS(root)

if __name__ == "__main__":
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
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
    # // -3   -4   -13
    # //     /       \
    # //    -2       -2

    print(f"What is the smallest value in this binary tree ? {treeMinValue(a)}")