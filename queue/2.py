class Queue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, data):
        self.items.append(data)
 
    def dequeue(self):
        if len(self.items)>0:
            return self.items.pop(0)
    def leng(self):
        return len(self.items)
    
    def getItem(self):
        output = self.items
        return output

firstqueue = Queue()
secondqueue = Queue()
lastqueue = Queue()
time1 = 0
time2 = 0
data,time = input('Enter people and time : ').split()
for i in data:
    firstqueue.enqueue(i)
for i in range(1,int(time)+1):
    if time1 == 3 and not secondqueue.is_empty():
        secondqueue.dequeue()
        time1 = 0
    if time2%2 == 0  and not lastqueue.is_empty():
        lastqueue.dequeue()
    if len(secondqueue.getItem())<5 and not firstqueue.is_empty():
        secondqueue.enqueue(firstqueue.dequeue())
    else:
        if not firstqueue.is_empty():
            lastqueue.enqueue(firstqueue.dequeue())
    time1+=1
    if not lastqueue.is_empty():
        time2+=1
    print(f'{i} {firstqueue.getItem()} {secondqueue.getItem()} {lastqueue.getItem()}')

    
