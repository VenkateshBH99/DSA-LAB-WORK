class Stack:
	 

 def __init__(self):
	    self.items=[]
 def push(self,x):
        self.items.append(x)
        return

 def isEmpty(self):
		if self.items==[]:
			return True
		return False

 def pop(self):
		if(self.isEmpty()):
			return str("Stack is empty")
		return self.items.pop()

 def top(self):
		if(self.isEmpty()):
			return float("Stack is empty")
		return self.items[len(self.items)-1]
	



    
