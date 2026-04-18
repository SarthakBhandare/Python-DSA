# DNF (Dutch National Flag) Algorithm 
# The DNF algorithm is a sorting algorithm that sorts an array of three distinct values (often represented as 0, 1, and 2) in linear time.
# The algorithm uses three pointers to partition the array into three sections: one for each distinct value.

def dnf_sort(arr):
    
    n = len(arr)
    low = 0
    mid = 0
    high = n - 1

    while mid < high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]  # Swap arr[low] and arr[mid]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    return arr      

arr = [0,2,1,2,1,1,0,0,2]

print(dnf_sort(arr))
    