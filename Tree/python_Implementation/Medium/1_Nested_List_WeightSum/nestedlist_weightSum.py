def depthSumInverse(nestedList: list[NestedInteger]) -> int:
        
    # Pass 1:
    # 1) Find the Max Depth from the Nested List
    def FindMaxDepth(nestedlist):
        maxDepth = 1
        for list_ in nestedlist:
            # We will only call the DFS if and only if we encounter a list and ignore integer because only a list's depth will increment, ignore empty list's depth
            if not list_.isInteger() and list_.getList():
                maxDepth = max(maxDepth, 1 + FindMaxDepth(list_.getList()))
                
        return maxDepth
    
    maxD = FindMaxDepth(nestedList)
    # return maxD
    # Pass 2:
    # 2) Multiply each integer in nestedList by its weight = maxDepth - (the depth of the integer) + 1
    def MultipleWeight(nestedlist, maxDepth, depth):
        s = 0
        
        for list_ in nestedlist:
            if list_.isInteger():
                s += list_.getInteger() * (maxDepth - depth + 1) 
            else:
                s += MultipleWeight(list_.getList(), maxDepth, depth+1)
                
        return s
    s = MultipleWeight(nestedList, maxD, 1)
    
    return s
        