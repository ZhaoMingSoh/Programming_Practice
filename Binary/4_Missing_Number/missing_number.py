# Sort the nums and check the presence of each number in the range [0,n] using a forloop
def missingnumber(nums : list[int]):
    nums.sort()
    s = 0
    for i in nums:
        if i == s:
            s += 1
        else:
            break
    
    return s

# Xor technique -> res = len(nums) ^ (i ^ nums[i])
def missingnumber_XOR(nums : list[int]):
    res = len(nums)
    for i in range(len(nums)):
        res ^= (i ^ nums[i])
    return res

# Sum technique
def missingnumber_SUM(nums : list[int]):
    s_1 = sum(nums)
    s_2 = 0
    for i in range(len(nums)+1):
        s_2 += i
    return s_2 - s_1

if __name__=="__main__":
    nums = [3,0,1]
    print(f"The missing number from this array {nums} is {missingnumber_SUM(nums)} as the range is between [0,{len(nums)}].")