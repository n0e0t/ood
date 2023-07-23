'''
หลังจากกฤษฎาล้างจานเสร็จ ก็ได้มาเล่นเกมส์ที่กำลังเป็นที่นิยมทั่วโลกในตอนนี้   
Microsoft Flight Simulator ?  Fall Guys ?  Valorant ?  ผิดทั้งหมดกฤษฎาได้กล่าวไว้  
เกมที่กำลังเป็นที่นิยมคือ Color Crush ต่างหาก   โดยเกมนี้จะเป็นการนำสีมาเรียงต่อกัน 
โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน เช่น  A B B B A  -> A A 
เนื่องจาก B เรียงติดกัน 3 ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  
โดยถ้าหากมีการระเบิดตั้งแต่ 2 ครั้งขึ้นไปจะแสดง Combo ขึ้นมา

  โดยเมื่อการระเบิดสิ้นสุดลงให้แสดงลำดับของสีที่เหลือจากขวาไปซ้าย

1. Enter Input : G H H H H P
    3
    PHG
2. Enter Input : L C C X X X C D
    2
    DL
    Combo : 2 ! ! !
3. Enter Input : C C C
    0
    Empty
'''

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