def longestConsecutive(nums: list[int]) -> int:
    numsSet = set(nums)

    longest = 0

    for num in numsSet:
        # Find the starting sequence - when num-1 does not exist for this num, then it is a starting sequence
        if (num - 1) not in numsSet:
            length = 0 
            # Find the longest consecutive sequence of the current num by continously adding 1 to it untill it no longers exist in the set.
            while (num + length) in numsSet:
                length += 1
            if longest < length:
                longest = length
                
    return longest

if __name__ == "__main__":
    # 99(X) <- 100 -> 101(X), so 100 is a starting sequence with the longest consecutive sequence of 1.
    # 3(X) <- 4 , it is not a starting sequence since we can find its predescessor.
    # 0(X) <- 1, it is a starting sequence and the longest consecutive sequence of this number is 4. 
    nums = [100,4,200,1,3,2]
    nums2 = [0,3,7,2,5,8,4,6,0,1]

    print(f"What is the length of the longest sequence in this {nums} ? {longestConsecutive(nums)}")
    print(f"What is the length of the longest sequence in this {nums2} ? {longestConsecutive(nums2)}")