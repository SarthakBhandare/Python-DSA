# juggling algorithm to Right rotate an array by d positions
# Time Complexity: O(n)
# Space Complexity: O(1)

from math import gcd

def rotate(arr,d):
    n = len(arr)
    gcdvalue = gcd(n,d%n)
    
    for i in range(gcdvalue):
        temp = arr[i]
        j = i
        while True:
            k = (j - d) % n # for right rotation, use (j - d) % n and for left rotation, use (j + d) % n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
            
        arr[j] = temp
        
    return arr 

arr = [1,2,3,4,5,6,7]
print(rotate(arr,2)) 