#数据结构--双端队列
#定义双端队列数据类型
class Dequeue:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return self.items==[]
    def enqueueFront(self,item):
        self.items.append(item)
    def enqueueRear(self,item):
        self.items.insert(0,item)
    def dequeueFront(self):
        return self.items.pop()
    def dequeueRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

#利用双端队列进行回文词的判断
def palchecker(astring):
    chardeque=Dequeue()
    for char in astring:
        chardeque.enqueueFront(char)
    stillOK=True
    while chardeque.size()>1 and stillOK:
        if chardeque.dequeueFront() !=chardeque.dequeueRear():
            stillOK=False
    return stillOK
print(palchecker('radar'))
print(palchecker('beautiful'))