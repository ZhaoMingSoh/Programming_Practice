import math

def find_minimum_in_rotated_sorted_array(nums : list[int]):
    ptr_l = 0
    ptr_r = len(nums)-1
    m = math.floor((ptr_l+ptr_r)/2)
    result = nums[m]

    while ptr_l <= ptr_r:
        m = math.floor((ptr_l+ptr_r)/2)
        if nums[ptr_l] < nums[ptr_r]:
            result = min(result, nums[ptr_l])
        result = min(result, nums[m]) 
        if nums[m] >= nums[ptr_l]:
            ptr_l = m+1
        else:
            ptr_r = m-1

    return result

# Method 2 : Key point is to find the pivot (the boundary at which point the value no longer increases).
#           - Use binary search, identify where the smallest value could be, either in the right or left subarray by checking the middle value against the left and right values.
#           - if m > l and m > r, then the smallest value will be in the left subarray (vice versa). [most important condition]
def find_minimum_in_rotated_sorted_array_2(nums : list[int]):
    left = 0
    right = len(nums)-1

    while left <= right:
        m = math.floor((left+right)/2)
        if m > 0 and nums[m] < nums[m-1]:
            return nums[m]
        if nums[m] >= nums[left] and nums[m] > nums[right]:
            print(left)
            left = m + 1
        else:
            right = m - 1
        
    return nums[m]

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    # print(f"smallest val : {find_minimum_in_rotated_sorted_array(nums)}")
    print(f"smallest val : {find_minimum_in_rotated_sorted_array_2(nums)}")