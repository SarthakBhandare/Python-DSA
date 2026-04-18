# Maximum Sum Rectangle in a 2D Matrix.
import sys
matrix = [[3, 8, 9, 1, 3],[-4, -1, 1, 7, -6], [-2, -3, 8, 1, -1]]

n = len(matrix)
m = len(matrix[0])
ans = -sys.maxsize - 1


def kadane(arr):
    currSum = 0
    maxSum = -sys.maxsize - 1
    for x in arr:
        currSum = max(x, currSum + x)
        maxSum = max(maxSum, currSum)
    return maxSum

for i in range (m):
    temp = []
    for j in range(n):
        temp.append(matrix[j][i])

    print(temp)

    ans = max(ans, kadane(temp))
    print(ans)

    for j in range(i+1,m):
        for k in range(n):
            temp[k] += matrix[k][j]

        print(temp)
        ans = max(ans, kadane(temp))
        print(ans)

    print("________________________________")

print(ans)


