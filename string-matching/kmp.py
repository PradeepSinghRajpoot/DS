def prefixTable(pattern):
    plen = len(pattern)
    F = [0]*plen
    k=0;

    for q in range(1, plen):
        while k>0 and pattern[k] != pattern[q]:
            k = F[k-1]

        if pattern[k] == pattern[q]:
            k = k + 1

        F[q] = k

    
    return F



def kmp(text, pattern):
    tlen = len(text)
    plen = len(pattern)
    F = prefixTable(pattern)
    print (F)
    q=0;


    for t in range(tlen):
        while q>0 and pattern[q] != text[t]:
            q = F[q-1]

        if pattern[q] == text[t]:
            q = q + 1

        if q == plen:
            return t-plen+1


    return -1;




print ("abcdefgabcabc", "abcabc", kmp("abcdefgabcabc", "abcabc"))


