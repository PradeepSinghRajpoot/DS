#! /usr/bin/python3

s3 = 'spam'
s3 = list(s3);

s1 = [1, 2, 5, 6, 7]

s1[2:3] = [100, 200]

s2 = range(100, 200, 10);

a1 = [1, 2, 3, 4, 5];
a2 = a1.copy();

print (a1+a2);

print (a1 * 3);

print (range(len(s1)));



for x in s1 :
    print (x);

print('-' * 10);
for x1 in s2:
    print (x1);
print('-' * 10);

print(a2.pop(2))

s3.remove('m');
print (s3);
