from collections import OrderedDict

# Method 1 : OrderedDict
class LRUCache(OrderedDict):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1
        
        self.move_to_end(key) # Once we get the particular key, it becomes more recently used than other keys in the OrderedDict, so it needs to be moved to the end of the OrderedDict.
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key) # Since we already have the particular key, it becomes more recently used than other keys in the OrderedDict, so it needs to be moved to the end of the OrderedDict.
        self[key] = value # New key will be placed at the end of OrderedList to reflect recency.
        if len(self) > self.capacity:
            self.popitem(last = False)

# commands = ["LRUCache","put","put","get","put","get","put","get","get","get"]
# values = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

# obj = None
# for i in range(len(commands)):
#     print(obj)
#     if commands[i] == "LRUCache":
#         obj = LRUCache(values[i][0])
#     elif commands[i] == "put":
#         obj.put(values[i][0], values[i][1])
#     else:
#         print(obj.get(values[i][0]))

# Method 2 : HashMap + DoubleLinkedList
# Time Complexity : O(1) - put and get
# Space Complexity : O(n)
class Node:
    def __init__(self) -> None:
        self.key = 0
        self.value = 0
        self.next = None
        self.prev = None
    
class LRUCache_:
    def __init__(self, capacity = 0) -> None:
        self.capacity = capacity
        self.size = 0
        self.cache = {}

        # Head and Tail Nodes
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeAtHead(self):
        """
        Always remove node from the head - signify least recently used
        """
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        return node

    def addNodeAtTail(self, node):
        """
        Always add a node to the tail end - signify most recently used
        """
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        return

    def removeNode(self, node):
        """
        remove a certain node from the doubly linked list
        """
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        return

    def move_to_end(self, node):
        """
        move a certain node that is being get and put to the tail end of the node - signify most recently used
        """
        self.removeNode(node)
        self.addNodeAtTail(node)
        return

    def get(self, key):
        """
        1) always get the node from the cache first to check if it is there
            a) if it is there, return the node value and move it to the tail end
            b) if it is not there, return -1
        """
        # print(self.cache)
        node = self.cache.get(key, None)
        if not node:
            return -1
        else:
            self.move_to_end(node)
        return node.value

    def put(self, key, value):
        """
        In the cache : {key : node},
        1) always get the node from the cache first to check if it is there
            a) if it is not there, new node - add from the tail end.
            b) if it is there, old node - needs to move to the back to signify it is more recently used than the rest.
        """
        node = self.cache.get(key)
        if not node:
            new_Node = Node()
            new_Node.key = key
            new_Node.value = value

            self.cache[key] = new_Node
            self.addNodeAtTail(new_Node)

            self.size += 1

            if self.size > self.capacity:
                delete_Node = self.removeAtHead()
                del self.cache[delete_Node.key]
                self.size -= 1
        else:
            node.value = value
            self.move_to_end(node)
        # print(self.cache)
        return
    
    def Print(self):
        curr = self.head
        while curr != None:
            print(f"{curr.key} : {curr.value}", end=",")
            curr = curr.next
        
commands2 = ["LRUCache","put","put","get","put","get","put","get","get","get"]
values2 = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

doubly_LinkedList = None
for i in range(len(commands2)):
    if commands2[i] == "LRUCache":
        doubly_LinkedList = LRUCache_(values2[i][0])
    elif commands2[i] == "put":
        doubly_LinkedList.put(values2[i][0], values2[i][1])
        doubly_LinkedList.Print()
        print()
    elif commands2[i] == "get":
        print(doubly_LinkedList.get(values2[i][0]))

