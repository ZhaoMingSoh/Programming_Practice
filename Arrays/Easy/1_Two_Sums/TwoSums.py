# Method 1 : Using 2 forloops, take the sum of an element i with each of the element j and compare the sum to the target value to determine the index of the elements that add to it.
# Time complexity : O(n^2)
def two_sums(nums : list[int], target : int):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
           if target == (nums[i]+nums[j]):
               return i, j

# Method 2 :  Use hashing table - take the difference between "each element and the target value", check if the difference exist in the dictionary (a.k.a : hashtable).
#                                 if it doesn't exist, add the element and its index into the hashtable.
# Time Complexity : O(n)
def hashing_two_sums(nums, target):
    h = dict()
    for i, num in enumerate(nums):
        if target - num in h:
            return [h[target - num], i]
        h[num] = i



if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(f"[Method 1] : index of the sum of the target({target}) = {two_sums(nums = nums, target = target)}")
    print(f"[Method 2] : index of the sum of the target({target}) = {hashing_two_sums(nums, target)} ")


