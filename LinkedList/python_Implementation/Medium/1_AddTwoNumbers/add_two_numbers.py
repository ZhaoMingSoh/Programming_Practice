class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# The key lies in the while condition where we would keep going until l1 == None, l2 == None and carry == 0 -> we have finished exploring l1 and l2 and there is no carry to be carried over.
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # Always start with a dummy node for convenience
    dummyNode = ListNode(0)
    currentNode = dummyNode
    carry = 0

    while l1 != None or l2 != None or carry != 0:
        # set x or y to 0 if l1 or l2 is None.
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        sum = x + y + carry
        # // is math.floor(division)
        carry = sum//10
        newNode = ListNode(sum%10)
        # Update the currNode
        currentNode.next = newNode
        currentNode = newNode
        # set l1 or l2 to None if l1.next or l2.next is None.
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummyNode.next

# Recursive :
def traverse_Recur(head : ListNode):
    if head == None:
        return

    print(head.val)
    traverse_Recur(head.next)

