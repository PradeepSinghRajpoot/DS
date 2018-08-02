def quick_sort(A, low, high):
    if low < high:
        pivot = partition(A, low, high)
        quick_sort(A, low, pivot-1)
        quick_sort(A, pivot+1, high)



def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            swap(alist, leftmark, rightmark)

    swap(alist, first, rightmark)

    return rightmark


def swap(A, x, y):
    t = A[x]
    A[x] = A[y]
    A[y] = x

x = [10, 5, 6, 8, 9, 12, 15]
print (x)
quick_sort(x, 0, len(x)-1 )
print (x,)
