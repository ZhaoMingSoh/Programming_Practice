class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# DFS - Recursive
def DFS(node, target):
    # Base cases : 
    if node == None: # traverse through the tree
        return False

    # If target node found, return True
    if node.val == target:
        return True

    # Will always Go left - will only return if and only if the target node is found - this will go all the way up to the root call, else it doesn't return anything other than traversing
    if DFS(node.left, target) == True:
        return True
    # Will always Go right
    if DFS(node.right, target) == True:
        return True
    
    return False
# BFS - Iterative
def BFS(node, target):
    if node == None:
        return False
    # Queue - LIFO
    queue = [node]

    while len(queue) != 0:
        cur_Node = queue.pop()

        if cur_Node.val == target:
            return True

        if cur_Node.left != None:
            queue.insert(0, cur_Node.left)
        if cur_Node.right != None:
            queue.insert(0, cur_Node.right)
        
    return False

def treeIncludes(root, target):
    # DFS - way
    # return DFS(root, target)

    # BFS - way
    return BFS(root, target)

if __name__ == "__main__":
    #               a
    #             /   \
    #            b     c
    #           / \     \
    #          d   e     f
    #             /       \
    #            g         h
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    h = Node("h")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    print(f"Is f in the binary tree ? {treeIncludes(a, 'f')}")
    print(f"Is f in the binary tree ? {treeIncludes(a, 'p')}")
    print(f"Is f in the binary tree ? {treeIncludes(None, 'b')}")