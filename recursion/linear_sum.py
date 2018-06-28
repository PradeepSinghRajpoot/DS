#! /usr/bin/python3

# @Author - Pradeep Singh Rajpoot
#

def linear_sum(S,n):
    if (n==0):
        return 0
    else:
        print(S[n-1])
        return linear_sum(S, n-1) + S[n-1]

x = [ 2, 3, 4, 5 ]

print (x)
print( linear_sum(x, len(x) ) )
