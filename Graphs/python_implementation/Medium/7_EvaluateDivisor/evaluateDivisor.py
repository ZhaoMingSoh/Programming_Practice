from collections import defaultdict
# DFS : Backtracking
def calcEquation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    # 1) Build the Graph from the equation -> an adjacency list
    graph = defaultdict(dict)

    def backtrack(cur_node, target_node, cumul_prod, visited):
        visited.add(cur_node)
        # This is to deal with unconnected nodes
        ret = -1
        
        # If we found the target, return the current cumulative product to the previous node
        if cur_node == target_node:
            return cumul_prod, True

        for neigh, val in graph[cur_node].items():
            if neigh in visited:
                continue                                                                                                                                                                                      
            ret, state = backtrack(neigh, target_node, cumul_prod*val, visited) # get the return value of the cumulative product if and only if the target is found, else it will stay as -1
            print(ret)
            
            # If we found the target, keep returning the result all the way up to the top
            if state == True:
                return ret, True
            
        return ret, False

        # Leetcode Implementation
        # visited.add(curr_node)
        # ret = -1.0
        # neighbors = graph[curr_node]
        # if target_node in neighbors:
        #     ret = acc_product * neighbors[target_node]
        # else:
        #     for neighbor, value in neighbors.items():
        #         if neighbor in visited:
        #             continue
        #         ret = backtrack_evaluate(
        #             neighbor, target_node, acc_product * value, visited)
        #         if ret != -1.0:
        #             break
        # visited.remove(curr_node)
        # return ret


    for (dividend, divisor),value in zip(equations, values):
        # 2 ways connection between nodes : normal, inverse
        # We are creating dict within dict : {'a': {'b': 2.0}, 'b': {'a': 0.5, 'c': 3.0}, 'c': {'b': 0.3333333333333333}}
        graph[dividend][divisor] = value
        graph[divisor][dividend] = 1/value
    
    # 2) Evaluate each query via backtracking (DFS) - by verifying if there exists a path from divident to divisor
    result = []
    for dividend, divisor in queries:
        # Case 1) either node does not exist, the result would be invalid
        if dividend not in graph or divisor not in graph:
            cumul_prod = -1
        # Case 2) The src and target are the same node
        elif dividend == divisor:
            cumul_prod = 1
        # Case 3) A path exist between the src and target
        else:
            # Prevent infinite loop as there exists a 2 way connection between nodes
            visited = set()
            cumul_prod = backtrack(dividend, divisor, 1, visited)[0]
        result.append(cumul_prod)

    return result


if __name__ == "__main__":
    equations, values, queries = [["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    print(f"The answers to {queries} are {calcEquation(equations, values, queries)}")
    equations2, values2, queries2 = [["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    equations3, values3, queries3 = [["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]
    equations4, values4, queries4 = [["a","b"],["c","d"]], [1.0,1.0], [["a","c"],["b","d"],["b","a"],["d","c"]]
    print(f"The answers to {queries4} are {calcEquation(equations4, values4, queries4)}")

    d = {'a': {'b': 2.0}, 'b': {'a': 0.5, 'c': 3.0}, 'c': {'b': 0.3333333333333333}}
    print(d['b'])