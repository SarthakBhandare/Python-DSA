# list = [1,2,3,4,5,"om","sarthak"]

# print(list)
# print(list[6])
# print(list[4:-1])

# len = len(list)
# print("Length of the list:", len)

# list.append("python")   # appending "python" at the end of the list.
# print(list)

# list.insert(2, "java") # inserting "java" at index 2.
# print(list)

# list.remove("om")     # removing "om" from the list.
# print(list)

# list.pop(3)          # removing element at index 3.
# print(list)

# list[1] = "c++"     # changing element at index 1 to "c++".
# print(list)

# list.clear()        # clearing the entire list.
# print(list)

# list = [1,2,3,4,5,6,7,8,9,10]
# print(list[0:9:2])

# mylist = [ele for ele in range (1,11)] # generating a list of numbers from 1 to 10 using list comprehension.
# print(mylist)

# list = [1,2,3,4,5,6,7,8,9,10] # reversing the list using slicing.
# print(list[::-2])

# list1 = [int(ele) for ele in input("Enter the numbers as a String: ").split()] # taking input as a string and converting it to a list of integers using list comprehension.
# print(list1)

mylist = []

n = int(input("Enter the number of elements you want to add to the list: "))
for i in range(n):
    element = input("Enter elemment : ")
    mylist.append(element)

print("The list you entered is: ", mylist)