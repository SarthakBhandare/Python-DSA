# Quick Sort
# Time Complexity: O(n log n) average case, O(n^2) worst case
# Space Complexity: O(log n)
# Quick Sort is a divide-and-conquer algorithm that picks an element as a pivot and partitions the given array around the picked pivot.

def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    # Choose the rightmost element as pivot
    pivot = arr[high]
    
    # Index of smaller element (indicates right position of pivot)
    i = low - 1
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(f"Pivot {pivot} placed at position {i + 1}: {arr}")
    print("----------------------------------")
    return i + 1

# Example usage
arr = int(input("Enter the number of elements in the array: "))
mylist = [int(ele) for ele in input("Enter the elements of the array: ").split()]
quick_sort(mylist, 0, len(mylist) - 1)
print("Sorted array is:", mylist)
