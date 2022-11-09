def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:
    allPaths = []
    # Bottom Up approach : Backtracking - incrementally build candidates to the solutions by finding the solution to the subproblems
    #                       - Classic DFS algorithm for DAG
    #                       - When to remove the candidates from the backtracking list that tracks the path from the source to the target so far ? 
    def DFS_Recur(graph, node, path_SoFar, target):
        if node == target:
            allPaths.append(list(path_SoFar))
            path_SoFar.pop() # **
            return
        
        for neigh in graph[node]:
            path_SoFar.append(neigh)
            DFS_Recur(graph, neigh, path_SoFar, target)

        path_SoFar.pop() # **
        return
    
    DFS_Recur(graph, 0, [0], len(graph1)-1)
    return allPaths

if __name__ == "__main__":
    # Directed Acyclic Graph
    graph1 = [[1,2],[3],[3],[]]
    print(f"All paths from source : 0 to target : {len(graph1)-1} are {allPathsSourceTarget(graph1)}")
    graph2 = [[4,3,1],[3,2,4],[3],[4],[]]
  
