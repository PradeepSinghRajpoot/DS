#! /usr/bin/python3

s1 = { 'a' : 'a1', 'b' : 'b1', 'c' : 'c1' };

print (len(s1));
print ('a' in s1);
print ('x' in s1);
print (s1.values());

for x in s1:
    print(x);

for x in s1.values():
    print(x);

for (k,v) in s1.items():
    print (k,'=',v)

