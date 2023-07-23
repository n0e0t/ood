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
    
word, first = input("Enter code,hint : ").split(",")
rs = Queue()
for ch in word:
    rs .enqueue(chr(ord(ch)+ord(first)-ord(word[0])))
    print(rs.getItem())

