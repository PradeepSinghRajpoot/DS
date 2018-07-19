class HashTable:
    def __init__(self):
        self.size = 11;
        self.slots = [None] * self.size
        self.data = [None] * self.size


    def hash(self, key):
        return key % self.size

    def rehash(self, oldhash):
        return (oldhash+1) % self.size


    def put(self, key, value):
        hashvalue = self.hash(key)

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key;
            self.data[hashvalue] = value;
        else:
            if (self.slots[hashvalue] == key):
                self.data[hashvalue] = value;
            else:
                nextslot = self.rehash(hashvalue)
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)
                    
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key;
                    self.data[nextslot] = value;
                else:
                    self.data[nextslot] = value;
        

    def get(self, key):
        data = None
        found = False
        stop = False

        start = self.hash(key)
        position = start 

        if (self.slots[position] == key):
            found = True
            data=self.data[position]
        else:
            while self.slots[position] != None and not found and not start:
                print(position, self.slots[position])
                if (self.slots[position] == key):
                    found = True
                    data=self.data[position]
                else:
                    position = self.rehash(position)
                    if (position == start):
                        stop = True
           
        return data

    def __getitem__(self, key):
        return self.get(key);

    def __setitem__(self, key, value):
        return self.put(key, value)


h = HashTable();
h[12] = 'cat'
h[44] = 'dog'
h[33] = 'rat'
h[80] = 'mat'
h[92] = 'hat'

print (h)
print (h.slots)
print (h.data)
print ('12', h[12])
print ('92', h[92])


