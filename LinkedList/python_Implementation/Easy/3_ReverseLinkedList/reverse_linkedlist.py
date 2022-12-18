class Node:
    def __init__(self, val, next = None) -> None:
        self.val = val
        self.next = next

def recur_traver(head):
    if head == None:
        return
    print(head.val)
    recur_traver(head.next)
    return

def reverseLinkedList(prev, current):
    if current == None:
        return
    next = current.next
    current.next = prev
    prev = current
    reverseLinkedList(prev, next)
    return

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")

A.next = B
B.next = C
C.next = D

reverseLinkedList(None, A)
recur_traver(D)
