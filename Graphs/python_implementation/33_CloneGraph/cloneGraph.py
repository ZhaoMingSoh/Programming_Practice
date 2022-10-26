class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: 'Node') -> 'Node':
    # Deals with the case when the node is Null
    if not node :
        return node

    # HashTable that maps the old Node to the new Node
    OldToNew = {}
    
    def BFS():
        queue = [node]

        # The starting node to traverse
        copyNode = Node(node.val) # create a copy of the starting node
        OldToNew[node] = copyNode # store it in the hashmap

        while len(queue) != 0:
            curNode = queue.pop() 
            curNodeClone = OldToNew[curNode]

            # Go through the neighbours of the popped node
            for neigh in curNode.neighbors:
                curCloneNeigh = Node()
                print(neigh.val)
                if neigh in OldToNew: # If the neighbor node is already in the hashmap
                    curCloneNeigh = OldToNew[neigh] # assign the corresponding copy of the neighbor node
                else:
                    queue.insert(0, neigh)
                    curCloneNeigh.val = neigh.val
                    OldToNew[neigh] = curCloneNeigh
                # Assign the copy of the neighbors to the Clone Node
                curNodeClone.neighbors.append(curCloneNeigh)

        return OldToNew[node] # return the clone node

    def DFS(node):
        if not node:
            return node

        curCloneNeigh = Node()

        # The 2 conditions to always check :
        if node in OldToNew:
            return OldToNew[node]
        else:
            # If the neighbouring node is not inside the HashMap, clone it and add to the HashMap
            newCloneNode = Node(node.val)
            OldToNew[node] = newCloneNode 
        
        # Explore the currently selected node
        for neigh in node.neighbors:
            # Eventually the HashMap will be populated with all the nodes, during the returning time of the recursion, append the return neighbouring nodes to the parent node
            curCloneNeigh = DFS(neigh)
            OldToNew[node].neighbors.append(curCloneNeigh)

        # Once finished appending a node's neighbours, return that node to the its parent node. 
        return OldToNew[node]

    return DFS(node)

# Time Complexity : 
#   E = # Edges
#   V = # Nodes
#   O(E*V) - worst case : there is only a single graph components and we have to explore all of its nodes.
# Space Complexity : 
#   O(E*V)
if __name__ == "__main__":
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    allNodes = []
    cloneNodes = []

    # Create all the Nodes and store their address in an Array
    for n in range(len(adjList)):
        N = Node()
        N.val = n+1
        allNodes.append(N)

    # Initialise all the neighbors of each Node from the adjList
    for n in range(len(adjList)):
        for neigh in adjList[n]:
            allNodes[n].neighbors.append(allNodes[neigh-1])
    
    for n in range(len(allNodes)):
        for neigh in allNodes[n].neighbors:
            print(f"Node {allNodes[n].val} : {neigh.val}")
        print("----------------")

    # We actually only need to pass in the starting node where the algorithm will clone out the entirety of the original graph thorugh exploring all the nodes.
    cloneStartingNode = cloneGraph(allNodes[0])
    print(f"{allNodes[0].val} : {allNodes[0].neighbors}")
    print(f"{cloneStartingNode.val} : {cloneStartingNode.neighbors}")


