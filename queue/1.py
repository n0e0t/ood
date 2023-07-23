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
    
    def __str__(self):
        output = ""
        if not self.is_empty():
            for item in self.items:
                output += str(item) + ' '
        else:
            output = 'Empty'
        return output
    

queue = Queue()
data = input('Enter Input : ').split(',')
for i in data:
    if len(i) == 1:
        if not queue.is_empty():
            print(queue.dequeue(), 0)
        else:
            print(-1)
    else:
        value = i.split()[1]
        queue.enqueue(value)
        print(queue.leng())
print(queue)