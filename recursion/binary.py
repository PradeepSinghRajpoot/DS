
result = []
def binary(A, n):
    if (n<1):
        result.append( ', '.join([ str(x) for x in A]))
    else:   
        A[n-1] = 0
        binary(A, n-1)
        A[n-1] = 1
        binary(A, n-1)


A = [ None ] * 3

print (A)
binary(A, 3)

print(result)
