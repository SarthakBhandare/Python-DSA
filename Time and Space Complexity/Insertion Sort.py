# Insertion Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

def insertion_sort(arr):
    # Traverse from the second element to the last element
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
        print(f"Inserted {key} at position {j + 1}: {arr}")
        print("----------------------------------")
    return arr

# Example usage                                                                                                                                                                                                 
arr = int(input("Enter the number of elements in the array: "))
mylist = [int(ele) for ele in input("Enter the elements of the array: ").split()]
sorted_arr = insertion_sort(mylist)
print("Sorted array is:", sorted_arr)
