# n = int(input("Enter a number: "))

# ans = 1
# for i in range(1, n + 1):
#     ans *= i

# print(ans) 



def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

ans = factorial(5)

print(ans) 