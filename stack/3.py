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
    return self.item[-2:]
result = stack()
values = input('Enter Input : ').split()
combos = 0

for i in values :
    c=0
    while  len(result.item)>=2 and result.isEmpty() == False and result.ontop()[0] == i and result.ontop()[1] == i:
        result.pop()
        result.pop()
        combos += 1
        c=1
    if  c == 0:
        result.item.append(i)

print(len(result.item))
if len(result.item) > 0:
    print(''.join(result.item[::-1]))
if len(result.item) == 0:
    print('Empty')
if combos > 1:
    print(f'Combo : {combos} ! ! !')