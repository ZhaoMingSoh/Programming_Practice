# Edge list of a graph
from pickle import FALSE
from re import I


edges = [
  ['i', 'j'],
  ['k', 'i'],
  ['m', 'k'],
  ['k', 'l'],
  ['o', 'n']
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

# 2) Depth first search - 
# How to prevent cyclic search ?
#   - mark each traversed node as visited.
def hasPath_DFS(graph, src, des):
    visited = set()
    stack = list(src)

    while len(stack) != 0:
        print(stack)
        curr_node = stack.pop()

        if curr_node == des :
            return True

        # Most important algo is this : where only during the addition of the neighbouring nodes do we check if the node is already visited.
        for neigh in graph[curr_node]:
            if neigh in visited:
                continue
            stack.append(neigh)
        
        visited.add(curr_node)

    return False

if __name__ == "__main__":
    graph_1 = convertEdge_AdjacencyList(edges)
    src = "o"
    des = "n"
    print(f" Does the undirected graph have a path from {src} to {des} ? {hasPath_DFS(graph_1, src, des)}")


