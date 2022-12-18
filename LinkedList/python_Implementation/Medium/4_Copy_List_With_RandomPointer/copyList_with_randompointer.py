class Node:
    def __init__(self, val, next = None, random = None) -> None:
        self.val = val
        self.next = next
        self.random = random

def print_LinkedList(node):
    if node == None:
        return
    print(node.val, end=" ")
    print_LinkedList(node.next)

visitedHash = {}
# Approach 1 - Intuitive : the random pointers in the linked list makes it so that cycles may exist, therefore it becomes a graph problem, use DFS(bottom up) + visited dict to solve it.
# Time Complexity : O(n)
# Space Complexity : O(n)

def copyRandomList_Intuitive(head):

    if head == None:
        return None

    # If we have already processed the current node, then we simply return the cloned version of it - deal with random pointers
    if head in visitedHash:
        return visitedHash[head]

    # create a new node - first time encoutering the node
    # with the value same as old node.
    node = Node(head.val, None, None)

    # Save this value in the hash map. This is needed since there might be
    # loops during traversal due to randomness of random pointers and this would help us avoid them.
    visitedHash[head] = node

    # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
    # Thus we have two independent recursive calls.
    # Finally we update the next and random pointers for the new node created - it will updated only after the next pointers have been exhausted (bottom up approach)
    node.next = copyRandomList_Intuitive(head.next)
    node.random = copyRandomList_Intuitive(head.random)

    return node
visitedHash.clear()

# Approach 3 - Iterative
# Time Complexity : O(n)
# Space Complexity : O(1)
def copyRandomList_Constant(head):
    if not head:
        return head
    
    # 1) Creating a new weaved list of original and copied nodes.
    ptr = head
    while ptr != None:
        # Cloned node
        cloned_Node = Node(ptr.val)

        # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
        cloned_Node.next = ptr.next
        ptr.next = cloned_Node
        ptr = ptr.next.next
    
    # 2) Use the original nodes' random pointers to assign references for cloned nodes.
    ptr = head
    while ptr != None:
        ptr.next.random = ptr.random.next if ptr.random else None
        ptr = ptr.next.next
    
    # 3) Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
    new_head = head.next
    old_List_ptr = head
    new_List_ptr = head.next

    while old_List_ptr != None:
        old_List_ptr.next = old_List_ptr.next.next
        new_List_ptr.next = new_List_ptr.next.next if new_List_ptr.next else None

        old_List_ptr = old_List_ptr.next
        new_List_ptr = new_List_ptr.next
    
    return new_head

A = Node('A')
B = Node('B')
C = Node('C')

A.next = B
B.next = C

A.random = C
B.random = A

# new_Node = copyRandomList_Intuitive(A)
# print_LinkedList(new_Node)
# print()

new_Node_2 = copyRandomList_Constant(A)
print_LinkedList(new_Node_2)
print()



