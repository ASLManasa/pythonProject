"""def power(base,exp):
    if (exp == 1):
        return base;
    else:
        return (base*power(base,exp-1))
print(power(2,4))"""


def linearsearch(array, x):
    for i in (0, len(array)):
        if (array[i] == x):
            return i


array = [1, 2, 3, 4, 5]
x = 2
linearsearch(array, x)
