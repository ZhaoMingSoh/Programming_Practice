def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    nums_1_copy = nums1.copy()
    p1, p2, p = 0, 0, 0

    for p in range(m+n):
        # The p2 >= n is there to ensure that 
        #   - when nums_1_copy elements are exhausted where p1 < m no longer holds, it forces the rest of the elements in nums2 to be added to the remainding nums1 indexes.
        #   - when nums1 length is 0 and nums2 length is 1, it forces the element from nums2 to be added to nums1.
        if p2 >= n or (p1 < m and nums_1_copy[p1] < nums2[p2]):
            nums1[p] = nums_1_copy[p1]
            p1 += 1
        else:
            nums1[p] = nums2[p2]
            p2 += 1

        print(f"p1:{p1},p2:{p2},p:{p},{nums1}")
    


if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    merge(nums1, m, nums2, n)
    print(f"Merging sorted array {[1,2,3,0,0,0]} and {nums2} equals {nums1}")

    nums1_1 = [1]
    nums2_1 = []
    merge(nums1_1, 1, nums2_1, 0)
    print(f"Merging sorted array {[1]} and {[]} equals {nums1_1}")

    nums1_2 = [0]
    nums2_2 = [1]
    merge(nums1_2, 0, nums2_2, 1)
    print(f"Merging sorted array {[0]} and {[1]} equals {nums1_2}")
