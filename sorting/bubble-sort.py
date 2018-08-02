def bubble_sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) -1 ):
            if a[j] > a[j+1]:
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp


    return a

a  = [ 2, 4, 1, 8, 7]
print (a)
print (bubble_sort(a))
