# Selection Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Selection Sort is a simple sorting algorithm that divides the input list into two parts: the sublist of items already sorted, which is built up from left to right at the front (left) of the list, and the sublist of items remaining to be sorted that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost element, and moving the sublist boundaries one element to the right.

def selection_sort(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        print(f"Swapped {arr[min_idx]} and {arr[i]}: {arr}")
        print("----------------------------------")
    return arr

# Example usage
arr = int(input("Enter the number of elements in the array: "))
mylist = [int(ele) for ele in input("Enter the elements of the array: ").split()]
sorted_arr = selection_sort(mylist)
print("Sorted array is:", sorted_arr)
