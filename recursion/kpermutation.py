
def generateKLengthStrings(chars, prefix, k):
    
    result = []

    if (k == 0):
        result.append(prefix)
        return result

    for c in chars:
        newprefix = prefix + c;

        x = generateKLengthStrings(chars, newprefix,  k-1)
        result = result + x

    return result


chars = ['a','b','c','d','e']

parr = generateKLengthStrings(chars, '', 2 )

print('parr', parr)
