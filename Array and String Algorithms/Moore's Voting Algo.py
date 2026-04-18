# Moore's Voting Algorithm
# The Moore's Voting Algorithm is used to find the majority element in an array, which is the element that appears more than half the time.
# The algorithm works in two phases: candidate selection and verification.

# Method 1: Using Sorting

# def majority_element(nums):
#     num.sort()  # Sort the array
    
#     majority_element = num[0]
#     max_count = 0
#     count = 0
    
#     for i in range(len(num) - 1):
#         if num[i] != num[i + 1]:
#             if max_count < count:
#                 majority_element = num[i]
#                 max_count = count
#             count = 1
#         else:
#             count += 1
    
#     # Check the last element
#     if max_count < count:
#         majority_element = num[-1]
        
#     return majority_element


# num = [1,3,3,1,1,3,3]
# print(majority_element(num))  # Output: 3

# Method 2: Using Moore's Voting Algorithm

def majority_element(nums):
    majority_element = -1
    votes = 0
    
    for i in nums:
        if votes == 0:
            majority_element = i
            votes = 1
        else:
            if i == majority_element:
                votes += 1
            else:
                votes -= 1

    votes = 0
    for i in nums:
        if majority_element == i:
            votes += 1

    if votes > len(nums) // 2:
        return majority_element
    
    return -1  # Return -1 if there is no majority element

num = [1,3,3,1,1,3,3,1]
print(majority_element(num))  # Output: -1 (since there is no majority element)