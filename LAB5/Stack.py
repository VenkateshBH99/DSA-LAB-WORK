class Stack:
    def __init__(self):
        self.items=[]
    def push(self,x):
        return self.items.append(x)
    def pop(self):
        if self.items==[]:
            return print('stack is empty')
        return self.items.pop()
    def top(self):
        if self.items==[]:
            return None
        return self.items[len(self.items)-1]
    def isEmpty(self):
        if self.items==[]:
            return True
        return False
