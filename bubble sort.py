## bubble sort


def bubble(l):
    for i in range(len(l), 1, -1):
        for j in range(1, i):
            if l[j - 1] > l[j]:
                l[j], l[j - 1] = l[j - 1], l[j]
    return l


# print(bubble([int(x) for x in input("Enter the list of numbers separated by spaces: ").split()]))


def foo(l):
    l = bubble(l)
    for i in range(len(l)):
        if l[i] == int(l[i]):
            l[i] = int(l[i])
    return l


print(foo([float(x) for x in input("Enter the values separated by spaces: ").split()]))
