graph1 = {
  0: ['8', '1', '5'],
  1: ['0'],
  5: ['0', '8'],
  8: ['0', '5'],
  2: ['3', '4'],
  3: ['2', '4'],
  4: ['3', '2']
}

graph2 = {
  1: ['2'],
  2: ['1','8'],
  6: ['7'],
  9: ['8'],
  7: ['6', '8'],
  8: ['9', '7', '2']
}

graph3 = {
  3: [],
  4: ['6'],
  6: ['4', '5', '7', '8'],
  8: ['6'],
  7: ['6'],
  5: ['6'],
  1: ['2'],
  2: ['1']
}

graph4 = {
  0: ['4','7'],
  1: [],
  2: [],
  3: ['6'],
  4: ['0'],
  6: ['3'],
  7: ['0'],
  8: []
}

def DFS_Iter(graph, current):
    visited = set()
    # DFS - undirected graph
    stack = list([current])

    while len(stack) != 0:
        currNode = stack.pop()
        for neigh in graph[currNode]:
            print(neigh)
            if int(neigh) in visited:
                continue
            stack.append(int(neigh))
        visited.add(currNode)
    
    return visited.copy()

def DFS_Recur(graph, current, visited = None):
    if visited == None:
        visited = set()
    
    if current in visited:
        return

    visited.add(current)

    for neigh in graph[current]:
        DFS_Recur(graph, int(neigh), visited)

    return visited.copy() # It will return when the component is fully explored.

def largestComponent(graph):
    listOfNodes = list(graph.keys())
    visited = set()
    visited_2 = set()
    componentSize = 0

    for node in listOfNodes:
        if int(node) in visited:
            continue
        visited_2 = DFS_Recur(graph, int(node))
        if len(visited_2) > len(visited):
            componentSize = len(visited_2)
        visited = visited_2.copy()
        
    return componentSize

if __name__ == "__main__":
    # Just compare the size of the visited set of each components to each other and select the largest one
    print(f"The largest component of {graph2} is {largestComponent(graph2)}")