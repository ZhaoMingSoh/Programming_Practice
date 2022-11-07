# Idea : (only works for sorted array) use 2 pointers left and right which start from either ends, take the diff from the smallest value on the left and compare the diff to the largest value on the right,
# move the left pointer if the diff is too big, so that we could find a smaller diff that is contained in the array, else move the right pointer to find the 2nd operand.
def twoSums_II(numbers : list[int], target : int):
    left = 0
    right = len(numbers)-1

    while left < right:
        diff = target - numbers[left]
        if diff == numbers[right]:
            return [left+1,right+1]
        elif diff < numbers[right]: # the 2nd operand may exist on the right
            right -= 1
        elif diff > numbers[right]: # the 2nd operand will not exist but we can try with larger value on the left
            left += 1
    
    return []

if __name__=="__main__":
    numbers = [2,7,11,15]
    target = 20
    print(f"index for sum of {target} is {twoSums_II(numbers, target)}")