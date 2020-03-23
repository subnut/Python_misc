## insertion sort

def insertion(l):
    for i in range(1,len(l)):
        for j in range(i,0,-1):
            if l[j]>=l[j-1]:
                break
            l[j],l[j-1]=l[j-1],l[j]
    return l

print(insertion([int(x) for x in input("Enter the list of numbers separated by blankspace: ").split()]))