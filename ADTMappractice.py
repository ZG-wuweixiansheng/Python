#映射抽象数据类型
class HashTable:
    def __init__(self):
        self.size=11
        self.slots=[None]*self.size
        self.data=[None]*self.size
    def hashfunction(self,key):
        return key%self.size
    def rehash(self,oldhash):
        return (oldhash+1)%self.size
    def put(self,key,data):
        hashvalue=self.hashfunction(key)
        if self.slots[hashvalue]==None:
            self.slots[hashvalue]=key
            self.data[hashvalue]=data
        else:
            if self.slots[hashvalue]==key:
                self.data[hashvalue]=data
            else:
                nextslots=self.rehash(hashvalue)
                while self.slots[nextslots] !=None and  self.slots[nextslots] != key:
                    nextslots=self.rehash(nextslots)
                if self.slots[nextslots]==None:
                    self.slots[nextslots]=key
                    self.data[nextslots]=data
                else:
                    self.data[nextslots]=data
    def get(self,key):
        startslot=self.hashfunction(key)
        data=None
        found=False
        stop=False
        position=startslot
        while self.slots[position] != None and not stop and not found:
            if self.slots[position]==key:
                found=True
                data=self.data[position]
            else:
                position=self.rehash(position)
                if position==startslot:
                    stop=True
        return data





