row = int(input("Enter the value of rows: "))
columns = int(input("Enter the value of colunms: "))
print('Size of the matrix: {} x {} '.format(row, columns))
matrix = []
for i in range(row):
    array = []
    for j in range(columns):
        array.append(int(input()))
    matrix.append(array)

print("Original Matrix:")
for i in range(row):
    for j in range(columns):
        print(matrix[i][j], end=" ")
    print()
print("Transpose of Matrix ")
for i in range(row):
    for j in range(columns):
        print(matrix[j][i], end=" ")
    print()
