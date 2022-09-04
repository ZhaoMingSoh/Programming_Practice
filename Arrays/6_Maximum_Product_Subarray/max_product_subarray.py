import math

# Method 1 : O(n)
# Dynamic Programming approach, for each element we're gonna keep track of 2 arrays
#                               - dp_max[nums[0]]
#                               - dp_min[nums[0]]
#                               if current_element > 0:
#                                  dp_max[i] = max(dp_max[i-1]*nums[i],nums[i]) -> (dp_max[i-1]*nums[i]) = the product of the elements so far multiply by the current element
#                                  dp_min[i] = min(dp_min[i-1]*nums[i],nums[i])
#                               elif current_element < 0:
#                                  dp_max[i] = max(dp_min[i-1]*nums[i],nums[i]) -> - * - = +
#                                  dp_min[i] = min(dp_max[i-1]*nums[i],nums[i]) -> + * - = -
def max_product_subarray_linear(nums : list[int]):
    dp_max =[0]*len(nums)
    dp_min =[0]*len(nums)

    dp_max[0] = dp_min[0] = nums[0]

    for i in range(1,len(nums)):
        if nums[i] > 0:
            dp_max[i] = max(dp_max[i-1]*nums[i], nums[i])
            dp_min[i] = min(dp_min[i-1]*nums[i], nums[i])
        else:
            dp_max[i] = max(dp_min[i-1]*nums[i], nums[i])
            dp_min[i] = min(dp_max[i-1]*nums[i], nums[i])
    
    return max(dp_max)

# Method 2: Space complexity of O(1)
def max_product_subarray_linear_2(nums : list[int]):
    dp_max = dp_min = nums[0]
    absolute_max = -math.inf

    for i in range(1,len(nums)):
        if nums[i] > 0:
            dp_max = max(dp_max*nums[i], nums[i])
            dp_min = min(dp_min*nums[i], nums[i])
        else:
            dp_max = max(dp_min*nums[i], nums[i])
            dp_min = min(dp_max*nums[i], nums[i])

        if dp_max > absolute_max:
            absolute_max = dp_max

    return absolute_max

if __name__ == "__main__":
    nums = [2,3,-2,4]
    print(f"Max_Product : {max_product_subarray_linear(nums)}")
    print(f"Max_Product : {max_product_subarray_linear_2(nums)}")