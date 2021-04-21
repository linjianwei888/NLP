def squre(x):
    return x ** 2


a = [1, 2, 3, 4]
b = list(map(squre, a))
print(b)


def func(x):
    return x % 2 == 1


c = list(filter(func, [1, 2, 3, 4, 5, 6, 7, 8]))
print(c)
