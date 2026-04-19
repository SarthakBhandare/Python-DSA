# Bubble Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The process is repeated until the list is sorted.

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place, no need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(f"Swapped {arr[j+1]} and {arr[j]}: {arr}")
                print("----------------------------------")
    return arr  
# Example usage
arr = int(input("Enter the number of elements in the array: "))
mylist = [int(ele) for ele in input("Enter the elements of the array: ").split()]
sorted_arr = bubble_sort(mylist)
print("Sorted array is:", sorted_arr)
