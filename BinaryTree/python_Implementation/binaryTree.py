# Binary Tree 
# - at most 2 children per node
# - exactly 1 root
# - exactly 1 path between root and any node

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

#) Depth First Search
# DFS - node -> left -> right
def depthFirstValues(node):
    # In case, an empty tree is given
    if node == None:
        return []
    # Use stack -> LIFO
    stack = [node]
    
    result = []
    # Check if the stack is empty, if not keep popping off the top node then add in the popped node's right and left child (in this order).
    # Once the stack is empty, that means I have traverse through all the nodes in the binary tree.
    while len(stack) != 0:
        cur_Node = stack.pop()
        result.append(cur_Node.val)
        if cur_Node.right != None:
            stack.append(cur_Node.right)
        if cur_Node.left != None:
            stack.append(cur_Node.left)

    return result 

# left -> right -> node
def depthFirstValue_Recur(node):
    # Base case: empty node
    if node == None:
        return []
    
    leftNodes = depthFirstValue_Recur(node.left)
    rightNodes = depthFirstValue_Recur(node.right)
    
    return [node.val] + leftNodes + rightNodes

# 2) Breath First Search
def breathFirstValue(node):
    result = []
    if node == None:
        return []

    # Queue -> LIFO
    queue = [node]

    while len(queue) != 0:
        cur_Node = queue.pop()
        result.append(cur_Node.val)
        if cur_Node.left != None:
            queue.insert(0,cur_Node.left)
        if cur_Node.right != None:
            queue.insert(0,cur_Node.right)
        
    return result

# Binary tree Search
# PreOrder : n l r  
def DFS_PreOrder(node):
    if node == None:
        return
    print(node.val)
    DFS_PreOrder(node.left)
    DFS_PreOrder(node.right)

    return

# InOrder : l n r
def DFS_InOrder(node):
    if node == None:
        return

    DFS_InOrder(node.left)
    print(node.val)
    DFS_InOrder(node.right)
    
    return

# PostOrder : l r n
def DFS_PostOrder(node):
    if node == None:
        return

    DFS_PostOrder(node.left)
    DFS_PostOrder(node.right)
    print(node.val)
    
    return

if __name__ == "__main__":
    # Initialise all the binary nodes
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    
    # Build a binary tree
    #      a
    #     / \
    #    b   c
    #   / \   \
    #  d   e   f
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    print(f"DFS Iterative : {depthFirstValues(a)}")
    print()
    print(f"DFS Recursive : {depthFirstValue_Recur(a)}")
    print()
    print(f"BFS : {breathFirstValue(a)}")
    print("Binary Search :")
    print(f"PreOrder : {DFS_PreOrder(a)}")
    print(f"InOrder : {DFS_InOrder(a)}")
    print(f"PostOrder : {DFS_PostOrder(a)}")
