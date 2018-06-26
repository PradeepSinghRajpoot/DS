#! /usr/bin/python3

a = 1
b = 2

a,b = b, a
print (a, b)

s = 'abc'
t = [0,1,2]

for i in zip(s,t):
    print (i)

print (list(zip(s, t)))

