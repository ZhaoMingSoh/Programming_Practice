graph1 = {
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}

graph2 = {
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}

graph3 = {
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
}

# Works on exploring the given graph components and populating the set with visited nodes.
# Iterative method :
def DFS_Iter(graph, visited, current):
    # DFS - undirected graph
    stack = list([current])

    while len(stack) != 0:
        currNode = stack.pop()
        for neigh in graph[currNode]:
            if neigh in visited:
                continue
            stack.append(neigh)
        visited.add(currNode)

# Recursive method :
def DFS_Recur(graph, visited, current):
    # Given that the current node is already visited, skip and go back to the previous function call.
    if current in visited:
        return
    
    visited.add(current)

    for neigh in graph[current]:
        DFS_Recur(graph, visited, neigh)
    
def connectedComponentCount(graph):
    count = 0
    listOfNodes = list(graph.keys())
    print(f"list of nodes : {listOfNodes}")
    visited = set()

    # Search through each node in the graph to determine if it is in the same component or not.
    for node in listOfNodes:
        print(f"node : {node} - visited : {visited}")

        # Check if a node is already visited first before running the DFS on that node.
        if node in visited:
            print(f"node : {node} - marked as visited")
            continue

        DFS_Recur(graph, visited, node) # the visited set will be populated as we run the DFS for each graph components.

        count += 1

    return count

if __name__ == "__main__":
    print(f"The number of connected components in {graph3} is {connectedComponentCount(graph3)}")