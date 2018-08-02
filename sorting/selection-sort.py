def selection_sort(a):
    for i in range(len(a) - 1):
        maxPos = 0
        for j in range(len(a) - i  ):
            if a[j] > a[maxPos]:
                maxPos = j;


        print ('exchangin value of ', str(maxPos) , ' and ' ,  str(j) )
        temp = a[j]
        a[j] = a[maxPos]
        a[maxPos] = temp
        print (a)

    return a

a  = [ 2, 4, 1, 8, 7]
print (a)
print (selection_sort(a))
