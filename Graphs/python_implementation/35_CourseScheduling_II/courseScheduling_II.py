def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    adjacencyList = {}
    def convertEdgesToAdjList():
        adjacencyList = {i : [] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            adjacencyList[crs].append(prereq)
        return adjacencyList
    
    output = []
    visited, cycle = set(), set()
    
    def DFS_Recur(crs):
        # A loop is detected because we ran into the crs twice when that crs has yet to finish its exploration
        if crs in cycle:
            return False

        # That crs is completely explored and no loop is found.
        if crs in visited:
            return True

        # Unvisited node and still have't finished exploring all of its neighbors - add into cycle
        cycle.add(crs)

        for neigh in adjacencyList[crs]:
            if DFS_Recur(neigh) == False:
                return False

        # We're able to explore all of the crs neighbors without loops
        cycle.remove(crs)
        visited.add(crs)
        output.append(crs)

        return output

    adjacencyList = convertEdgesToAdjList()

    for crs in range(numCourses):
        # If a loop is detected, return an empty output
        if DFS_Recur(crs) == False:
            return []
    
    # If no loop is detected, return the crs topological ordering output
    return output

if __name__ == "__main__":
    prerequisites = [[1,0],[0,1]]
    prerequisites2 = [[0,1], [0,2], [1,3], [1,4], [3,4]]
    prerequisites3 = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]

    print(f"The resulting order to finish all the courses from {prerequisites} is {findOrder(2, prerequisites)}")
    print(f"The resulting order to finish all the courses from {prerequisites2} is {findOrder(5, prerequisites2)}")
    print(f"The resulting order to finish all the courses from {prerequisites3} is {findOrder(20, prerequisites3)}")