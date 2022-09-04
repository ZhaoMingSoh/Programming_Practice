import math

# Use binary search, identify the left and right portion of the sorted array, then check if the target value is in them or not,
# (most important notes) : to take into account of the left value in left portion and the right value in the right portion.
def search_in_rotated_sorted_array(nums : list[int], target : int):
    left = 0
    right = len(nums) - 1

    while left <= right:
        m = math.ceil((left+right)/2)
        if target == nums[m]:
            return m

        # left portion of the sorted array
        if nums[left] <= nums[m]:
            if target > nums[m] or target < nums[left]:
                left = m + 1
            else:
                right = m - 1
        # right portion of the sorted array
        else:
            if target < nums[m] or target > nums[right]:
                right = m - 1
            else:
                left = m + 1
            
    return -1

if __name__ == "__main__":
    nums = [4,5,6,7,8,1,2,3]
    target = 8
    print(f"Target : {target} is at index : {search_in_rotated_sorted_array(nums, target)}")