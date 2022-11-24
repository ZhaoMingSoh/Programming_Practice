class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Iterative :
def traverse_Iter(head : Node):
    current_Node = head

    while current_Node != None:
        print(current_Node.val)
        current_Node = current_Node.next

# Recursive :
def traverse_Recur(head : Node):
    if head == None:
        return

    print(head.val)
    traverse_Recur(head.next)

if __name__ == "__main__":
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    traverse_Iter(a)
    print()
    traverse_Recur(a)
