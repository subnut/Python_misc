## shell_sort


def insertion(l, step):
    for i in range(1, len(l), step):
        for j in range(i, 0, -step):
            if l[j] >= l[j - step]:
                break
            l[j], l[j - step] = l[j - step], l[j]
    return l


def control(l):
    step = len(l) // 2
    while True:
        if step < 1:
            break
        l = insertion(l, step)
        step -= 1
    return l


# print(control([int(x) for x in input("Enter the list of numbers separated by spaces: ").split()]))


def foo(l):
    l = control(l)
    for i in range(len(l)):
        if l[i] == int(l[i]):
            l[i] = int(l[i])
    return l


print(foo([float(x) for x in input("Enter the values separated by spaces: ").split()]))
