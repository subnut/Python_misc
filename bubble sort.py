## bubble sort

def bubble(l):
    for i in range(len(l),1,-1):
        for j in range(1,i):
            if l[j-1]>l[j]:
                l[j],l[j-1]=l[j-1],l[j]
    return l

print(bubble([int(x) for x in input("Enter the list of numbers separated by blankspace: ").split()]))