class Hash:
    def __init__(self, text, size):
        self.size = size;
        self.text  = text;

        self.hashValue = 0;
        for t in range(0, self.size):
            self.hashValue += ord(text[t])

        self.init = 0;
        self.end = size;


    def hashedValue(self):
        return self.hashValue;

    def to_text(self):
        return self.text[self.init : self.end]        


    def rehash(self):
        if self.end < len(self.text):
            self.hashValue -= ord(self.text[self.init])
            self.hashValue += ord(self.text[self.end])
            self.init += 1
            self.end += 1;




def rabin_karp_search(text, pattern):

    plen = len(pattern)
    tlen = len(text)

    hashText = Hash(text, plen)
    hashPattern = Hash(pattern, plen)

    for i in range(tlen-plen+1):
        if hashText.hashedValue() == hashPattern.hashedValue():
            if hashText.to_text() == pattern:
                return i

        hashText.rehash();


    return -1


print ("pradeep", "deep", rabin_karp_search("pradeep", "deep")) 
