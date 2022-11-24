# Sort the nums and check the presence of each number in the range [0,n] using a forloop
def missingnumber(nums):
    nums.sort()
    s = 0
    for i in nums:
        if i == s:
            s += 1
        else:
            break
    
    return s

# Xor technique -> res = len(nums) ^ (i ^ nums[i])
def missingnumber_XOR(nums):
    res = len(nums)
    for i in range(len(nums)):
        res ^= (i ^ nums[i])
    return res

# Sum technique : If we take the difference between the sum of the nums that has all the supposed values lets say : nums = [0,1,2,3] from the given nums = [3,0,1], we can get the missing number
#               - This draws from the fact that all the nums list should always start from 0 to len(nums)-1.
def missingnumber_SUM(nums):
    s_1 = sum(nums)
    s_2 = 0
    for i in range(len(nums)+1):
        s_2 += i
    return s_2 - s_1

if __name__=="__main__":
    nums = [3,0,1]
    print(f"The missing number from this array {nums} is {missingnumber_XOR(nums)} as the range is between [0,{len(nums)}].")
    print(f"The missing number from this array {nums} is {missingnumber_SUM(nums)} as the range is between [0,{len(nums)}].")