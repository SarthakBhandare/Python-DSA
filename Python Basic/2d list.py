# grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # creating a 2D list (list of lists) to represent a grid.
# print(grid) 
# print(grid[0][1]) # accessing the element in the first row and second column (which is 2).

n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

grid = []
for i in range(n):
   grid.append([int(item) for item in input(f"Enter the elements of row {i+1}: ").split()])

print(grid)