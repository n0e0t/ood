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
       
    def size(self):
        return len(self.items)
           
    def __str__(self) -> str:
        return str(self.items)

ip = input('Enter Input : ').split('/')
data = ip[0].split(',')
cms = ip[1].split(',')

listdata = {}
for person in data:
    part,person_id = person.split()
    if part not in listdata:
        listdata[part] = []
    listdata[part].append(person_id)

listcm = {}
for cm in cms:
    if cm == 'D':
        is_found = False
        newlistcm = listcm.copy()
        for c in newlistcm:
            if listcm[c].size() == 0:
                continue
            else:
                print(listcm[c].dequeue())
                is_found = True
                break
        for c in newlistcm:
            if listcm[c].size() == 0:
                del listcm[c]
        if not is_found:
            print('Empty')
    else:
        addid = cm.split()[1]
        for c in listdata:
            if addid in listdata[c]:
                if c not in listcm:
                    listcm[c] = Queue()
                listcm[c].enqueue(addid)

