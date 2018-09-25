def permutation(string):
    result = []

    def permute(A, l, r):
        if(l==r):
            result.append(''.join(A))
        else:
            for i in range(l,r+1):
                A[l],A[i] = A[i],A[l]
                permute(A, l+1, r)
                A[l],A[i] = A[i],A[l]

    string = list(string)
    strlen = len(string)
    permute(string, 0, strlen-1)

    return result


print (permutation('ABC'))


