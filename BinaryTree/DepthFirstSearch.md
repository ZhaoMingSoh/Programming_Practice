# The pattern of using DFS to search a Binary Tree
1. The base case of node == Null always return 0 or nothing depending on the situation.
    - in the case of 3_TreeMinValue : find the min value in the binary tree
        - the base case for when node == Null : return +Infinity, we want to remove its effect from the algorithm altogether as +Infinity will never will be taken by minValue.
    - in the case of 5_RangeSum_Of_BST : find the sum of the range of value between [low, high]
        - the base case for when node == Null : return 0 so that it does not affect the total sum.
2. The algo will keep [moving to the left subtree] until the base case is hit before [moving to the right subtree] until the base case is hit then [move back to the root of the subtree.]
    - Bottom up approach :
        - in the case of 3_TreeMinValue : (PostOrder)
            - find the smallest val from the left subtree and the right subtree then compare it to the current root of the subtree before return the minValue.
        - in the case of 5_RangeSum_Of_BST : (InOrder)
            - keep going left until you hit the base case which will return a sum of 0, check if the current subtree root's node.val is in [low, high], then node.val + LeftSum, keep going right which will also return a sum of 0, then add node.val + LeftSum + RightSum and return to the previous call.