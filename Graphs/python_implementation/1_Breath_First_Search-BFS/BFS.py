# Present the graph in an adjacency list format
graph = {
    'a' : ['b','c'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
}

# Method 1 : Iterative Traversal
def Breath_First_Search(graph : dict):
    # Get all the keys from the graph dict
    key_list = list(graph.keys())

    # Uses the Queue (FIFO) to traverse the graph
    queue = [key_list[0]]

    while len(queue) != 0:
        curr_node = queue[len(queue)-1]
        queue.remove(curr_node)
        print(curr_node)
        for neigh in graph[curr_node]:
            queue.insert(0,neigh)

    return

# Method 2 : Recursive Traversal
    
if __name__ == "__main__":
    Breath_First_Search(graph)
