# Method 1 : sort the list into ascending orders and check if the adjacent elements are identical or not.
def detect_duplicate(nums : list[int]) -> bool:
    nums.sort()
    ptr_1 = 0
    ptr_2 = 1
    print(nums)
    while (ptr_1 <= len(nums)-2) and (ptr_2 <= len(nums)-1):
        if nums[ptr_1] == nums[ptr_2]:
            return True
        else:
            ptr_1 += 1
            ptr_2 += 1 

    return False

# Method 2 : Hashing, place each of the elements into the hash table and in the case where an element is already in the hash table,
#            we return true.
def detect_duplicate_hash(nums : list[int]) -> bool:
    table = dict()
    for i in range(len(nums)):
        if table.get(nums[i]) == None:
            table[nums[i]] = i
        else:
            return True

    return False


if __name__ == "__main__":
    nums = [1,3,4,2]
    print(f"Method 1 : Using 2 ptrs, result is {detect_duplicate(nums)}")
    print(f"Method 2 : Using a hash table, result is {detect_duplicate_hash(nums)}")