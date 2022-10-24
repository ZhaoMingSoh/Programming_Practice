# Present the graph in an adjacency list format
# Directed Graph
graph = {
    'a' : ['b','c'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
}
# graph = {
#     1 : [2,3],
#     2 : [4],
#     3 : [5],
#     4 : [3],
#     5 : [6],
#     6 : []
# }

# Method 1 : Iterative traversal
def depth_first_search(graph : dict):
    # Get all the keys from the graph dict
    key_list = list(graph.keys())

    # Uses the stack (LIFO) to traverse the graph
    stack = [key_list[0]]
    
    while len(stack) != 0:
        curr_node = stack.pop()
        print(curr_node)
        for neigh in graph[curr_node]:
            stack.append(neigh)

    return

# Method 2 : Recursive Traversal
def depth_first_search_r(graph : dict):
    # Get all the keys from the graph dict
    key_list = list(graph.keys())

    def dfs_helper(graph, source):
        print(source)
        # Recursive calls on the immediate neighbor
        for neigh in graph[source]:
            dfs_helper(graph,neigh)
        return

    dfs_helper(graph,key_list[0])
    return

if __name__ == "__main__":
    print(f"Iterative DFS traversal :")
    depth_first_search(graph)
    print(f"Recursive DFS traversal :")
    depth_first_search_r(graph)