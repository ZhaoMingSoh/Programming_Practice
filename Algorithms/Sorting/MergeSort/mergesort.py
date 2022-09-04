def merge(A : list[int], l : int, mid : int, h : int) -> list[int]:
    i, j = l , mid+1 
    C, k = [], l

    while i <= mid and j <= h:
        if A[i] < A[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(A[j])
            j += 1
        k += 1

    if i <= mid:
        for temp in range(i,mid+1):
            C.append(A[temp])
    elif j <= h:
        for temp in range(j,h+1):
            C.append(A[temp])

    return C

def mergeSort_Iterative(A : list[int], n : int):
    
    return

if __name__ == "__main__":
    A = [3,5,7,8,4,6,9,11]
    C = merge(A,0,3,len(A)-1)
    print(C)