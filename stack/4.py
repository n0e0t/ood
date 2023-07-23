class Stack:
    def __init__(self):
        self.ls=[]
    def push(self,new):
        self.ls.append(new)
    def pop(self):
        out = self.ls.pop()
        return out
    def isEmpty(self):
        if(len(self.ls)==0):
            return True
        else:
            return False
    def size(self):
        return len(self.ls)

def StackCalculator(data):
    stack = Stack()
    for func in data:
        if (func=='+'):
            x = stack.pop()
            y = stack.pop()
            stack.push(x+y)
        elif(func=='-'):
            x = stack.pop()
            y = stack.pop()
            stack.push(x-y)
        elif(func=='*'):
            x = stack.pop()
            y = stack.pop()
            stack.push(x*y)
        elif(func=='/'):
            x = stack.pop()
            y = stack.pop()
            stack.push(x//y)
        elif(func=='POP'):
            stack.pop()
        elif(func=='DUP'):
            x = stack.pop()
            stack.push(x)
            stack.push(x)
        elif(func=='PSH'):
            stack.push()
        elif(func.isalpha()):
            return 'Invalid instruction: '+func
        else:
            stack.push(int(func))
    if stack.isEmpty() == False:
        return int(stack.pop())
    else:
        return 0

class StackCalc:
    def __init__(self):
        self.ans = 0
    def run(self,arg):
        data = arg.split()
        self.ans = StackCalculator(data)
    def getValue(self):
        return self.ans
    
print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())