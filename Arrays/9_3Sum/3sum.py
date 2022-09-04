# This is when i!=j, i!=k, j!=k, the solution must not have duplicate triplets (solution must be unique)
def ThreeSum(nums : list[int]):
    nums.sort()
    result = []

    for i, a in enumerate(nums):
        left, right = i+1, len(nums)-1
        while left < right:
            triplet_sum = a + nums[left] + nums[right]
            if triplet_sum > 0:
                right -= 1
            elif triplet_sum < 0:
                left += 1
            else:
                res = [a,nums[left],nums[right]]
                if res not in result:
                    result.append(res)
                left += 1
            
    return result

# Fix the value of a and reduce the problem down to a two-sum problem for b and c. O(n^2) - forloop for a and whileloop for b and c.
# To make sure each solution added to the resulting array is unique, we skip them over by checking the current value with the previous.
def ThreeSum(nums : list[int]):
    nums.sort()
    result = []

    for i, a in enumerate(nums):
        # Skip over the same value like [-1,-1,2]
        if i > 0 and a == nums[i-1]:
            continue

        left, right = i+1, len(nums)-1
        while left < right:
            triplet_sum = a + nums[left] + nums[right]
            if triplet_sum > 0:
                right -= 1
            elif triplet_sum < 0:
                left += 1
            else:
                result.append([a,nums[left],nums[right]])
                left += 1 # keep continuing until left == right where thre loop will stop
                while nums[left] == nums[left-1] and left > right: # skip over the same value that has already been visited by the left-1. 
                    left += 1
                
    return result

if __name__ == "__main__":
    nums = [0,0,0,0]
    print(f"Distinct triplets that sum to 0 are {ThreeSum(nums)}")
