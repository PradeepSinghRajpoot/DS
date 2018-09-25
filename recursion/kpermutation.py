
def generateKLengthStrings(chars, prefix, k):
    
    result = []

    if (k == 0):
        result.append(prefix)
        return result

    for c in chars:
        newprefix = prefix + c;
        print('newprefix', newprefix, str( k-1))
        x = generateKLengthStrings(chars, newprefix,  k-1)
        result = result + x

    return result


chars = ['a','b','c','d','e']

parr = generateKLengthStrings(chars, '', 3 )

print('parr', parr)
