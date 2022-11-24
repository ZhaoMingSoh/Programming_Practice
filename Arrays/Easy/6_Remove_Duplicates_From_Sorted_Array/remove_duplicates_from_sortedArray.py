def removeDuplicates(nums) -> int:
    if nums == None:
        return 0
   
    insert_i = 1
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[insert_i] = nums[i]
            insert_i += 1
    
    return insert_i

def removeDuplicates_While(nums) -> int:
    l = r = 0
       
    while r < len(nums):
        # Skip duplicate until a non-duplicate is found, however, the r will still be at 1 index off from the newly found value.
        while r + 1 < len(nums) and nums[r+1] == nums[r]:
            r += 1

        # At the start : r will be at an index 1 before the new found value, thus, nums[l] = nums[r] of the same value in order to kick start the algo
        # At the second iteration : r will again be at an index 1 before the second new found value, but this time, r is first new found value before, so nums[l] = nums[r] of the last index of the first new found value
        nums[l] = nums[r]
        l += 1 # new insert index
        r += 1 # move to the newly found value index
        
    return l
        
if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    nums2 = [0,1,2]
    nums3 = [1,1,2]

    # print(f"The number of distinct duplicates for {nums} is {removeDuplicates(nums)} : {nums}")
    print(f"The number of distinct duplicates for {nums} is {removeDuplicates_While(nums)} : {nums}")
    # print(f"The number of distinct duplicates for {nums2} is {removeDuplicates(nums2)} : {nums2}")
    print(f"The number of distinct duplicates for {nums2} is {removeDuplicates_While(nums2)} : {nums2}")
    # print(f"The number of distinct duplicates for {nums3} is {removeDuplicates(nums3)} : {nums3}")
    print(f"The number of distinct duplicates for {nums3} is {removeDuplicates_While(nums3)} : {nums3}")