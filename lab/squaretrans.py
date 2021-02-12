def transpose(A):
    for i in range(N):
        for j in range(i + 1, N):
            A[i][j], A[j][i] = A[j][i], A[i][j]


print("Enter the row size : ")
r = int(input())
print("Enter the columns size : ")
c = int(input())
N = r
A = []
print("Matrix Original")
for i in range(r):
    arr = []
    for j in range(c):
        arr.append(int(input()))
    A.append(arr)
print()

print("Original Matrix:")
for i in range(N):
    for j in range(N):
        print(A[i][j], ' ', end=" ")
    print()

transpose(A)

print("Modified matrix is")
for i in range(N):
    for j in range(N):
        print(A[i][j], " ", end='')
    print()
