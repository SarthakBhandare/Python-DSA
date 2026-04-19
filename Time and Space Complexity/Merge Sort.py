# Merge Sort
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Merge Sort is a divide-and-conquer algorithm that divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements from either list
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    print(f"Merged {left} and {right}: {merged}")
    print("----------------------------------")
    return merged

# Example usage
arr = int(input("Enter the number of elements in the array: "))
mylist = [int(ele) for ele in input("Enter the elements of the array: ").split()]
sorted_arr = merge_sort(mylist)
print("Sorted array is:", sorted_arr)
