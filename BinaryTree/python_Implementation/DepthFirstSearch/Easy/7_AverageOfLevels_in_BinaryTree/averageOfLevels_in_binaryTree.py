class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfLevels(root: TreeNode) -> list[float]:
        count = []
        res = []
        average = []
 
        def DFS_Special(index, count, res, node):
            if node == None:
                return
            
            if len(count) < index + 1:
                count.extend([0])
            if len(res) < index + 1:
                res.extend([0])
                
            DFS_Special(index+1, count, res, node.left)
            DFS_Special(index+1, count, res, node.right)
                
            count[index] += 1
            res[index] += node.val
            
            return
        
        DFS_Special(0,count,res,root)
        
        for i in range(len(count)):
            average.append(res[i]/count[i])
            
        return average

if __name__ == "__main__":
    root = [3,9,20,None,None,15,7]
    treeNodes = [TreeNode(val=root[i]) for i in range(len(root)) if root[i] != None]
    # Build the binary tree   
    treeNodes[0].left = treeNodes[1]
    treeNodes[0].right = treeNodes[2]

    treeNodes[2].left = treeNodes[3]
    treeNodes[2].right = treeNodes[4]

    #     3
    #   /   \
    #  9     20
    #       /  \
    #      15   7

    print(f"The average in each level of the binary tree is {averageOfLevels(treeNodes[0])}")