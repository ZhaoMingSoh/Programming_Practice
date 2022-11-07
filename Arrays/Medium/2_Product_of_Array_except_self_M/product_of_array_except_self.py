def find_product_of_array_except_self(nums : list[int]) -> list[int]:
    answer = [0]*len(nums)
    temp = 1

    # Find the prefix of each element at index i, the prefix is a multiples of all the elements that come before it. Place it at the index of that element.
    for i in range(len(nums)):
        if i == 0:
            answer[i] = 1
        else:
            answer[i] = temp
        temp *= nums[i]

    temp = 1   

    # Find the postfix of each element at index i (from the end) - (same as prefix)
    for j in reversed(range(len(nums))):
        if j == len(nums)-1:
            answer[j] *= 1
        else:
            answer[j] *= temp
        temp *= nums[j]

    return answer

if __name__ == "__main__":
    nums = [1,2,3,4]
    print(find_product_of_array_except_self(nums))
