# Edge list of a graph
from pickle import FALSE


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

# 2) Depth first search
def hasPath_DFS(graph, src, des):
    
    return

if __name__ == "__main__":
    graph_1 = convertEdge_AdjacencyList(edges)
    print(graph_1)


