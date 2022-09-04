import math

# Method 1 : O(n^2) - we use 2 forloops to find all the subarrays and another loop to find the sum of those subarrays
# Find all the subarrays of an array
def find_all_subarrays(nums : list[int]) -> list[int]:
    subarrays = []

    for s in range(len(nums)):
        temparray = []
        for e in range(s,len(nums)):
            temparray.append(nums[e])
            subarrays.append(temparray[:])

    return subarrays

def find_maximum_subarray(nums : list[int]):
    subarrays = find_all_subarrays(nums)

    max_sum = -math.inf
    max_sum_index = None

    for i in range(len(subarrays)):
        local_sum = sum(subarrays[i])
        if local_sum > max_sum:
            max_sum = local_sum
            max_sum_index = i
        
    return subarrays[max_sum_index], max_sum

# Extending Method 1:
# Combine
def find_maximum_subarray_2(nums : list[int]) -> int:
    max_sum = -math.inf
    
    for s in range(len(nums)):
        temparray = []
        for e in range(s,len(nums)):
            temparray.append(nums[e])
            local_sum = sum(temparray)
            if local_sum > max_sum:
                max_sum = local_sum

    return max_sum

# Method 2 : O(n) - at each index of the array, we check the max(nums[i], current_sum) - ensure that we will get subarray with the max sum.
# ~~~ current_sum : the sum of all the elements of the subarray so far including the current element.
def find_maximum_subarray_linear(nums : list[int]) -> int:
    current_sum = 0
    max_sum = -math.inf
    
    for i in range(len(nums)):
        if i == 0:
            current_sum = nums[i]
        else:
            current_sum += nums[i]
            if current_sum < nums[i]:
                current_sum = nums[i]
            print(current_sum)
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(find_all_subarrays(nums))
    subarrays, max_sum = find_maximum_subarray(nums)
    # Method 1:
    print(f"Max_sum : {max_sum}, Subarray : {subarrays}")
    # Extending Method 1:
    print(f"Max_sum : {find_maximum_subarray_2(nums)}")
    # Method 2:
    print(f"Max_sum : {find_maximum_subarray_linear(nums)} ")


