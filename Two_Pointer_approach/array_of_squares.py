arr = [-4,-3,0,1,10]

def increasing_squares_sort(arr):
    squared_arr = list()
    ptr_1 = 0
    ptr_2 = len(arr) - 1

    while ptr_1 <= ptr_2:
        if abs(arr[ptr_1]) < abs(arr[ptr_2]):
            squared_arr.insert(0,arr[ptr_2]**2)
            ptr_2 -= 1
        else:
            squared_arr.insert(0,arr[ptr_1]**2)
            ptr_1 += 1

    return squared_arr

print(increasing_squares_sort(arr))