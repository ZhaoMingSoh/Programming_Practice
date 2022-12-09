class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def recursive_Iter(head):
    if head == None:
        return
    print(head.val, end='')
    recursive_Iter(head.next)
    return

# Two-Pass :
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    currentNode = head
    length = 0

    # Get the length of the linked-list
    while currentNode != None:
        length += 1
        currentNode = currentNode.next
    
    # Find the node before the nth node
    nth_Node_Before_Index = length - n
    currentNode = dummy
    for i in range(nth_Node_Before_Index):
        currentNode = currentNode.next

    # Remove the nth node
    currentNode.next = currentNode.next.next

    return dummy.next

# One-Pass : both pointers are seprated by n nodes apart
def removeNthFromEnd_OnePass(head : ListNode, n : int):
    # Cannot work for linked-list of size 1. (To work we need to employ this condition)
    if head.next == None and n == 0:
        return head.next
    dummy = ListNode(0)
    dummy.next = head
    nth_Node_After = dummy
    nth_Node_Before = dummy

    # Moves the first ptr to n+1
    for i in range(n+1):
        nth_Node_After = nth_Node_After.next

    # Maintain the gap by moving the second ptr until the first ptr arrives past the last node.
    while nth_Node_After != None:
        nth_Node_After = nth_Node_After.next
        nth_Node_Before = nth_Node_Before.next

    # Remove the nth node
    nth_Node_Before.next = nth_Node_Before.next.next

    return dummy.next

l1 = [1,2,3,4,5]
ListNodes = [ListNode(i) for i in l1]
p1, p2 = 0, 1
for i in range(len(ListNodes)):
    ListNodes[p1].next = ListNodes[p2]
    p1 += 1
    if p2 == len(ListNodes)-1:
        break
    p2 += 1
print("Before : ", end='')
recursive_Iter(ListNodes[0])
changed_l1 = removeNthFromEnd_OnePass(ListNodes[0], 2)
print("\nAfter : ", end='')
recursive_Iter(changed_l1)
print()

l2 = [1]
ListNodes2 = [ListNode(i) for i in l2]
print("Before : ", end='')
recursive_Iter(ListNodes2[0])
changed_l2 = removeNthFromEnd_OnePass(ListNodes2[0], 0)
print("\nAfter : ", end='')
recursive_Iter(changed_l2)
print()

l3 = [1,2]
ListNodes3 = [ListNode(i) for i in l3]
p1_3, p2_3 = 0, 1
for i in range(len(ListNodes3)):
    ListNodes3[p1_3].next = ListNodes3[p2_3]
    p1_3 += 1
    if p2_3 == len(ListNodes3)-1:
        break
    p2_3 += 1
print("Before : ", end='')
recursive_Iter(ListNodes3[0])
changed_l3 = removeNthFromEnd_OnePass(ListNodes3[0], 1)
print("\nAfter : ", end='')
recursive_Iter(changed_l3)
print()