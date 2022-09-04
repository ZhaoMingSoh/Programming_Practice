import math

def binary_search(arr : list[int], size : int, target : int):
    lwr = 0
    upr = size - 1

    while lwr <= upr:
        mid = math.floor((lwr + upr)/2)
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            upr = mid - 1
        elif target > arr[mid]:
            lwr = mid + 1

    return "Does not exist."

if __name__ == "__main__":
    array = [4,8,10,15,18,21,24,27,29]
    print(binary_search(array, len(array), 4))

