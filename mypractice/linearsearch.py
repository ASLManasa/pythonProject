def linear(arr, n, x):
    for j in range(0, x):
        if arr[j] == n:
            return i
    return -1


arr = []
for i in range(int(input("Enter the size of the array:"))):
    arr.append(int(input()))
print("Enter the value to be searched: ")
n = int(input())
x = len(arr)
answer = linear(arr, n, x)
if (answer == -1):
    print("not found")
else:
    print("found")
