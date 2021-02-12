from itertools import permutations


def permu(n):
    perm = permutations(n)
    print("All the permutation: ")
    for i in list(perm):
        print(''.join(i))


print("Enter the string: ")
n = str(input())
print("Given string: ")
print(n)
permu(n)
