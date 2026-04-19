# Time Complexity Examples
# time complexity is a measure of the amount of time an algorithm takes to complete as a function of the size of the input. It is often expressed using Big O notation, which describes the upper bound of the growth rate of an algorithm.

# O(1) - Constant Time
def constant_time(n): # This function takes constant time regardless of the input size
    return n * 2

# O(n) - Linear Time
def linear_time(n): # This function takes linear time as it iterates through all elements up to n
    total = 0
    for i in range(n):
        total += i
    return total

# O(n^2) - Quadratic Time
def quadratic_time(n): # This function takes quadratic time as it has nested loops that iterate through all pairs of elements up to n
    total = 0
    for i in range(n):
        for j in range(n):
            total += i * j
    return total

# O(log n) - Logarithmic Time
def logarithmic_time(n): # This function takes logarithmic time as it divides the input size by 2 in each iteration
    count = 0
    while n > 1:
        n //= 2
        count += 1
    return count


# Space Complexity Examples


# O(1) - Constant Space
def constant_space(n): # This function uses constant space as it only requires a fixed amount of memory regardless of the input size
    return n * 2

# O(n) - Linear Space
def linear_space(n): # This function uses linear space as it creates a list of size n   
    return [i for i in range(n)] 

# O(n^2) - Quadratic Space
def quadratic_space(n): # This function uses quadratic space as it creates a 2D list
    return [[0 for _ in range(n)] for _ in range(n)]

# O(log n) - Logarithmic Space
def logarithmic_space(n): # This function uses logarithmic space as it only requires a fixed amount of memory for the count variable
    count = 0
    while n > 1:
        n //= 2
        count += 1
    return count

# Master Theorem Example
def master_theorem_example(n): # This function has a time complexity of O(n log n) based on the Master Theorem
    if n <= 1:
        return 1
    else:
        return master_theorem_example(n // 2) + master_theorem_example(n // 2) + n