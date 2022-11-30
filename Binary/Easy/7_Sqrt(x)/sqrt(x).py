import math
# Binary Search
# target = 12
# nums = [-2,1,2,5,6,8,10,12]

# def BinarySearch(nums, target):
#     left = 0
#     right = len(nums)-1
#     mid = 0

#     while left <= right:
#         mid = math.floor((left + right) /2)
#         if nums[mid] == target:
#             return mid
#         if target < nums[mid]:
#             right = mid - 1
#         if target > nums[mid]:
#             left = mid + 1

#     return mid

# print(BinarySearch(nums, target))

# sqrt(x) = y , x = y * y
def mySqrt(x: int) -> int:
    # Starts from L = 1 to R = x/2 because the  0 <= sqrt(x) <= x/2.
    L = 1
    R = x/2
    ans = 0

    while L <= R:
        mid = int((L+R)/2)
        # print(f"L:{L}, mid:{mid}, R:{R}")
        if mid*mid == x:
            ans = int(mid)
            break
        # If y*y < x, this means y is too small so we're gonna make it bigger through discarding the smaller half of the numbers by setting L = mid + 1.
        # Note : The y value will almost always end up smaller than the x itself, therefore we cannot disregard the samller y as it could be the answer we're looking for.
        elif mid*mid < x:
            ans = int(mid)
            L = mid + 1
        else:
            R = mid - 1

    return ans
    
print(mySqrt(4))