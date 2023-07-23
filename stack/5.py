class Stack:
    def __init__(self):
        self.item = []
    def push(self,new):
        self.item.append(new)
    def pop(self,new):
        wh = self.item.index(new)
        self.item.pop(wh)
    def setItem(self,new):
        if new == '0':
            self.item = []
        else:
            self.item = new.split(',')
            self.item = [int(item) for item in self.item]
        
carpark = Stack()
print("******** Parking Lot ********")
m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
m,n = int(m),int(n)
### Enter Your Code Here ###
carpark.setItem(s)
if m > len(carpark.item) and o == 'arrive':
    if n in carpark.item:
        print(f'car {n} already in soi')
    else:
        carpark.push(n)
        print(f'car {n} arrive! : Add Car {n}')
elif m <= len(carpark.item) and o == 'arrive':
    if n in carpark.item:
        print(f'car {n} already in soi')
    else:
        print(f'car {n} cannot arrive : Soi Full')
elif o == 'depart' and len(carpark.item) == 0:
    print(f'car {n} cannot depart : Soi Empty')
elif o == 'depart' and len(carpark.item) > 0:
    if n in carpark.item:
        carpark.pop(n)
        print(f'car {n} depart ! : Car {n} was remove')
    else:
        print(f'car {n} cannot depart : Dont Have Car {n}')

print(carpark.item)


