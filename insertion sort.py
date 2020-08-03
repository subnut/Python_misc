## insertion sort


def insertion(l):
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            if l[j] >= l[j - 1]:
                break
            l[j], l[j - 1] = l[j - 1], l[j]
    return l


# print(insertion([int(x) for x in input("Enter the list of numbers separated by spaces: ").split()]))


def foo(l):
    l = insertion(l)
    for i in range(len(l)):
        if l[i] == int(l[i]):
            l[i] = int(l[i])
    return l


print(foo([float(x) for x in input("Enter the values separated by spaces: ").split()]))
