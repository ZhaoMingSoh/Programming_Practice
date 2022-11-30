import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Preorder traversal DFS : at each height, we recursively select the left most value as the root node for each subtrees.
def sortedArrayToBST(nums: list[int]) -> TreeNode:
    def helper(left, right):
        if left > right:
            return None
        # To ensure we're selecting the left most value of each portion of the nums as the root node
        p = math.floor((left+right)/2)
        root = TreeNode(nums[p])
        # Populate 
        root.left = helper(left, p-1)
        root.right = helper(p+1, right)

        return root

    return helper(0, len(nums)-1)

def dfs_In(node):
    if node == None:
        return
    
    dfs_In(node.left)
    print(node.val)
    dfs_In(node.right)

    return

if __name__ == "__main__":
    nums1 = [-10,-3,0,5,9]
    nums2 = [1,3]

    bst1 = sortedArrayToBST(nums1)
    print(f"The Preorder traversal of {nums1} will create a BST that looks like :")
    dfs_In(bst1)
    bst2 = sortedArrayToBST(nums2)
    print(f"The Preorder traversal of {nums2} will create a BST that looks like :")
    dfs_In(bst2)


