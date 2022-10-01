graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

graph2 = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

# DFS search
def dfs_hasPath(graph, src, des):
    if src == des:
        return True
    for neigh in graph[src]:
        if dfs_hasPath(graph, neigh, des) == True:
            return True
    return False

# BFS search
def bfs_hasPath(graph, src, des):
    queue = [src]
    while len(queue) > 0:
        curr_node = queue[len(queue)-1]
        if curr_node == des:
            return True
        queue.remove(curr_node)
        for neigh in graph[curr_node]:
            queue.insert(0,neigh)

    return False

if __name__ == "__main__":
    src = 'f'
    des = 'k'
    print("DFS")
    print(f"Does the path from {src} to {des} exist in the graph ? {dfs_hasPath(graph,src,des)}")
    print(f"Does the path from {'f'} to {'j'} exist in the graph ? {dfs_hasPath(graph,'f','j')}")
    print(f"Does the path from {'v'} to {'w'} exist in the graph ? {dfs_hasPath(graph2,'v','w')}")

    print("BFS")
    print(f"Does the path from {src} to {des} exist in the graph ? {bfs_hasPath(graph,src,des)}")
    print(f"Does the path from {'f'} to {'j'} exist in the graph ? {bfs_hasPath(graph,'f','j')}")
    print(f"Does the path from {'v'} to {'w'} exist in the graph ? {bfs_hasPath(graph2,'v','w')}")