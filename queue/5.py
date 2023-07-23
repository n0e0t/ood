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
    
    def __str__(self) -> str:
        return str(self.items)

width,height,room = input('Enter width, height, and room: ').split()
data = room.split(",")
final = []
went = []
queue = Queue()
found_f = False
for row in data:
    preroom = []
    for column in row:
        preroom.append(column)
        if column == 'F':
            went.append((row.index(column),data.index(row)))
            queue.enqueue((row.index(column),data.index(row)))
            found_f = True
    if len(preroom) != int(width):
        print('Invalid map input.')
        exit()
    final.append(preroom)
if len(final) != int(height):
    print('Invalid map input.')
    exit()
if not found_f:
    print('Invalid map input.')
    exit()

scan_set = [(0,-1),(1,0),(0,1),(-1,0)]
while not queue.is_empty():
    print('Queue:',queue)
    x,y = queue.dequeue()
    for setx,sety in scan_set:
        if y+sety >= 0 and y+sety < int(height) and x+setx >= 0 and x+setx < int(width):
            pos = final[y+sety][x+setx]
            if pos == 'O':
                print('Found the exit portal.')
                exit()
            elif pos == '_' and (x+setx,y+sety) not in went :
                went.append((x+setx,y+sety))
                queue.enqueue((x+setx,y+sety))
print('Cannot reach the exit portal.')