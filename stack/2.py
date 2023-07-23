class stack:
  def __init__(self):
    self.item = []

  def __len__(self):
    return len(self.item)

  def push(self,item):
    self.item.insert(0,item)

  def peek(self):
    if len(self) == 0:
      raise Exception("peek() called on empty stack.")
    return self.item[0]

  def pop(self):
    if len(self) == 0:
      raise Exception("pop() called on empty stack.")
    return self.item.pop()

  def __str__(self):
    return str(self.item)

  def isEmpty(self):
    if len(self.item)== 0:
        return True   
    else:
        return False

  def ontop(self):
    return self.item[-1]

values = input('Enter Input : ').split(',')
result = stack()

for i in values:
    w =  i.split()[0]
    while result.isEmpty() == False and int(result.ontop().split()[0]) < int(w):
        print(result.ontop().split()[1])
        result.pop()
    
    result.item.append(i)