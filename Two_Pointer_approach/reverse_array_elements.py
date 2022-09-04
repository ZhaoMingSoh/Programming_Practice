arr = [1,2,3,4,5,6]

def reverse_array_elements(arr):
    ptr_1 = 0
    ptr_2 = len(arr) - 1

    while ptr_1 < ptr_2:
        temp = arr[ptr_1]
        arr[ptr_1] = arr[ptr_2]
        arr[ptr_2] = temp
        ptr_1 += 1
        ptr_2 -= 1

    return arr

print(reverse_array_elements(arr))
