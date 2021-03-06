## quicksort


def quicksort(l):
    if len(l) > 1:
        p = l[0]  # pivot
        less = []
        more = []
        i = 0
        while True:
            try:
                if l[i] < p:
                    less.append(l.pop(i))
                if l[i] > p:
                    more.append(l.pop(i))
                if l[i] == p:
                    i += 1
            except IndexError:
                break
        less = quicksort(less)
        more = quicksort(more)
        l = less + l + more
    return l


# print(quicksort([int(x) for x in input("Enter the list of numbers separated by spaces: ").split()]))


def foo(l):
    l = quicksort(l)
    for i in range(len(l)):
        if l[i] == int(l[i]):
            l[i] = int(l[i])
    return l


print(foo([float(x) for x in input("Enter the values separated by spaces: ").split()]))
