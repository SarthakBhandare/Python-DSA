# KMP (Knuth-Morris-Pratt) Algorithm for Pattern Searching
# The KMP algorithm is an efficient string searching algorithm that uses preprocessing to create a longest prefix-suffix (LPS) array, which helps in avoiding unnecessary comparisons.
# Time Complexity: O(n + m), where n is the length of the text and m is the length of the pattern.
# Space Complexity: O(m) for the LPS array.
# The KMP algorithm consists of two main steps:
# 1. Preprocessing the pattern to create the LPS array.
# 2. Searching the pattern in the text using the LPS array to skip unnecessary comparisons.

def computeLPS(str ,lps):
    n = len(str)
    i = 1
    temp = 0
    
    while i < n:
        if str[i] == str[temp]:
            temp += 1
            lps[i] = temp
            i += 1
        else:
            if temp != 0:
                temp = lps[temp - 1]
            else:
                lps[i] = 0
                i += 1



def KMP(a, b):
    N = len(a)
    M = len(b)
    lps = [0] * M
    
    computeLPS(b, lps)
    
    i = 0 # index for text
    j = 0 # index for pattern
    
    while i < N:
        if a[i] == b[j]:
            i += 1
            j += 1
            
            if j == M:
                return i - j # pattern found at index (i - j)
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1 # pattern not found

a = "ababcababcabc"
b = "abc"

result = KMP(a, b)
print("Pattern found at index:", result)