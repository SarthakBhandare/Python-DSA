myList = []

def binary_search(start, end):
    global myList
    global target
    
    if end - start <= 1:
        if myList[start] == target:
            print("Element found at index: ", start)
            return
        elif myList[end] == target:
            print("Element found at index: ", end)
            return
        else:
            print("Element not found in the array.")
            return
        
    middle = (start + end) //2
        
    if myList[middle] > target:
        return binary_search(start, middle)
    
    return binary_search(middle, end)
    
        
n = int(input("Enter the size of the array: "))
target = int(input("Enter the target element: "))
myList = [int(ele) for ele in input("Enter the elements of the array: ").split()]
       
index = binary_search(0, n-1)

print(index)
    