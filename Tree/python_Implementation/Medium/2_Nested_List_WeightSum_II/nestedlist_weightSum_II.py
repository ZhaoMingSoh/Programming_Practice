def depthSum(nestedList: list[NestedInteger]) -> int:
    
    def DFS_Recur(nestedL, depth, s = 0):
        for list_ in nestedL:
            if list_.isInteger():
                s += list_.getInteger() * depth
            else:
                s = DFS_Recur(list_.getList(), depth + 1, s)
                
        return s

    return DFS_Recur(nestedList, 1)