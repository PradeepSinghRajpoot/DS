#! /usr/bin/python3

def is_reversed(s1,s2):
    x1=len(s1)
    x2=len(s2)
    result = False
    if (x1 == x2):
        result = True;
        i=0;
        j=x2;
        while(i < x2) :
            if s1[i] != s2[j-1] :
                result = False
                break
            i += 1;
            j -= 1;
    return result


s1 = 'pradeep'
s1 = 'xxx' + s1[2:7];
print (s1, '=', len(s1));

i=0;
while (i < len(s1)) :
    print (i, s1[i])
    i += 1

print('');
print(s1[0:4]);

print('stop', 'pots', is_reversed('xxxstop','pots'))

print ('kx' in 'pradeexxp');

for x in 'pradeep' :
    print (x);
