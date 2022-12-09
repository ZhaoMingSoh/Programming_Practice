from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
# Method 1 : 
# Time Complexity : O(n)
# Space Complexity : O(n) -> the queue
def connect(root: Node) -> Node:
    def BFS(root):
        q = deque([root])

        while len(q) != 0:
            # size of the current queue = the number of nodes at the current level
            size = len(q)

            # establish the next pointers for all of the nodes at the current level, by the time this finishes, we would have populated the queue with all of the nodes on the next level.
            for node in range(size):
                cur_node = q.popleft() 
                # Prevent setting the next right pointer beyond the end of a level because the queue can have 2 level of nodes any one time.
                if node < size-1:
                    cur_node.next = q[0]
                
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)

        return
    BFS(root)
    return

# Method 2 :
# Time Complexity : O(n)
# Space Complexity : O(1)
def connect_2(root: Node) -> Node:
    if root == None:
        return root

    leftmost = root
    while leftmost.left != None:
        head = leftmost
        # Setting the next right pointer for the nodes on the level N+1 when we're at still at level N
        # This helps get rid of the queue
        while head != None:
            # Connection 1 - set the next right pointer for the nodes that have the same parent
            head.left.next = head.right

            # Connection 2 - set the next right pointer for the nodes that have diff parent
            if head.next:
                head.right.next = head.next.left
            
            # Make use of the established next right pointer to go on to the next right node at the same level
            head = head.next
        # the leftmost node will always be the left child of the current leftmost node
        leftmost = leftmost.left
    
    return

def BFS_Iter(root):
    q = deque([root])

    while len(q) != 0:
        cur_Node = q.pop()

        print(cur_Node.next)
        print
    return


root = [1,2,3,4,5,6,7]
BST = [Node(i) for i in root]
BST[0].left = BST[1]
BST[0].right = BST[2]

BST[1].left = BST[3]
BST[1].right = BST[4]

BST[2].left = BST[5]
BST[2].right = BST[6]

connect(BST[0])