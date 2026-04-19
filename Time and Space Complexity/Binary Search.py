# Binary Search Algorithm
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Note: The array must be sorted for binary search to work correctly.

n = int(input("Enter the size of the array: "))
target = int(input("Enter the target element: "))
mylist = [int(ele) for ele in input("Enter the elements of the array: ").split()]

found = False
for i in mylist:
    if i == target:
        found = True
        break

if found == True:
    print("Element found in the array.")
else:
    print("Element not found in the array.")

