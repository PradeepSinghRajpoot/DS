def search(text, pat):
    found=False
    tlen = len(text)
    plen = len(pat)

    for t in range(tlen-plen+1):

        for p in range(plen):
            #print (text[t+p], pat[p])

            if text[t+p] != pat[p]:
                break;

        if p==plen-1:
            found = True


    return found


print ('pradeep', 'deep', search('pradeep', 'deep'));
print ('raj', 'aj', search('raj', 'aj'));
print ('abcdefg', 'mnop', search('abcdefg', 'mnop'));
