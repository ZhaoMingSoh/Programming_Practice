class Node:
    def __init__(self, val, next = None) -> None:
        self.val = val
        self.next = next

def getNodeVal(index, head, count):
    if head == None:
        return -1
    if count == index:
        return head.val
    val = getNodeVal(index, head.next, count + 1)
    return val

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")

A.next = B
B.next = C
C.next = D

print(getNodeVal(2,A,0))
        