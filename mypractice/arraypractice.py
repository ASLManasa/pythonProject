import array

arr = array.array('i', [1, 2, 3])
arr.append(23)
arr.reverse()
for j in range(0, 4):
    print(arr[j], end=" ")
