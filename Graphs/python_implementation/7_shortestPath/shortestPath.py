edges1 = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

edges2 = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

edges3 = [
  ['m', 'n'],
  ['n', 'o'],
  ['o', 'p'],
  ['p', 'q'],
  ['t', 'o'],
  ['r', 'q'],
  ['r', 's']
]

# 1) Convert edge list to an adjacency list
def convertEdge_AdjacencyList(edges):
    graph = {}
    
    for edge in edges:
        node_1, node_2 = edge
        # If the graph does not contain the node_1 and node_2 as keys, proceed to add them with an empty array as val
        if graph.get(node_1) == None:
            graph[node_1] = []
        if graph.get(node_2) == None:
            graph[node_2] = []
        # Assign each others to each others' array since they are connected
        graph[node_1].append(node_2)
        graph[node_2].append(node_1)

    return graph

# The best algo for shortest path finding is BFS - the first time it encounters the destination node, it also indicates the shortest path to it.
def BFS_ShortestPath(graph, src, des):
    visited = set() # keep track of visited nodes to prevent infinite loop
    queue = [{"node" : src, "distFromSrc" : 0}] 
    
    # The same as DFS for problem 4, 5 and 6
    while len(queue) != 0:
        curr_node = queue.pop()

        if curr_node['node'] == des:
            return curr_node["distFromSrc"]
        
        for neigh in graph[curr_node["node"]]:
            if neigh in visited:
                continue
            visited.add(neigh)
            queue.insert(0,{"node" : neigh, "distFromSrc" : curr_node["distFromSrc"] + 1})

    return None

# Time complexity is linear because it only goes through the graph once.
if __name__ == "__main__":
    graph1 = convertEdge_AdjacencyList(edges1)
    graph2 = convertEdge_AdjacencyList(edges2)
    graph3 = convertEdge_AdjacencyList(edges3)

    src = "w"
    des = "z"
    print(f'The shortest path from {src} to {des} in {graph1} is {BFS_ShortestPath(graph1, src, des)}')
    print(f'The shortest path from {"y"} to {"x"} in {graph1} is {BFS_ShortestPath(graph1, "y", "x")}')
    print(f'The shortest path from {"e"} to {"c"} in {graph2} is {BFS_ShortestPath(graph2, "e", "c")}')
    print(f'The shortest path from {"b"} to {"g"} in {graph2} is {BFS_ShortestPath(graph2, "b", "g")}')
    print(f'The shortest path from {"m"} to {"s"} in {graph3} is {BFS_ShortestPath(graph3, "m", "s")}')
