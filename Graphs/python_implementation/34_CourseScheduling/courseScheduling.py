def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    adjacencyList = {}

    # The adjacencyList is a bit special in the sense that the relationship between each node only goes 1. 
    #   1) [0,1] => to complete 0, need to complete 1 first; therefore the relationship looks like this
    #      0 ---> 1
    #   2) [0,1] [1,0]
    #      0 <---> 1
    def convertToAdjacencyList():   
        for n in prerequisites:
            node1, node2 = n
            if adjacencyList.get(node1) == None:
                adjacencyList[node1] = []
            if adjacencyList.get(node2) == None:
                adjacencyList[node2] = []
            adjacencyList[node1].append(node2)
        return

    def convertToAdjacencyList2():
        adjacencyList = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjacencyList[crs].append(pre)
        return adjacencyList
    
    visited = set()
    def DFS(node):
        if node in visited: # If a node is already in the visited set, this tells me a loop has been found, therefore it is impossible to finish all courses
            return False

        if len(adjacencyList[node]) == 0: # A course with no prerequisite is always able to be completed, therefore True
            return True
        
        # If neither 2 of the conditions were the case, then we are exploring a new node
        visited.add(node)
    
        # Explore the new node's neighbors
        for neigh in adjacencyList[node]:
            if not DFS(neigh): # Once a loop is detected, we keep returning false until the end
                return False
        visited.remove(node) # there could be multiple individual components that have the same courses but different prerequisites
        adjacencyList[node] = [] # We remove the already explored node to prevent repeats exploration of the same node which can be time consuming

        return True # If the neighbors were managed to be explored without any deadlocks, return true

    adjacencyList = convertToAdjacencyList2()
    
    # There could be multiple individual graph components, therefore we need to loop through all the courses
    for crs in range(numCourses):
        if not DFS(crs):
            return False
    
    # Second Way to do it via numbering system where 0 : unvisited, 1 : visited, 2 : processing
    # visited2 = [0] * numCourses

    # def DFS2(node):
    #     if visited2[node] == 1:
    #         return True
        
    #     if visited2[node] == 2:
    #         return False

    #     visited2[node] = 2

    #     for neigh in adjacencyList[node]:
    #         if not DFS2(neigh):
    #             return False
        
    #     visited2[node] = 1

    #     return True

    # for crs in range(numCourses):
    #     if not DFS2(crs):
    #         return False

    return True

if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    prerequisites2 = [[0,1], [0,2], [1,3], [1,4], [3,4]]
    prerequisites3 = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]

    print(f"Can all the courses be finished given this array of prerequisites : {prerequisites} ? {canFinish(numCourses, prerequisites)}")
    print(f"Can all the courses be finished given this array of prerequisites : {prerequisites2} ? {canFinish(5, prerequisites2)}")
    print(f"Can all the courses be finished given this array of prerequisites : {prerequisites3} ? {canFinish(20, prerequisites3)}")
