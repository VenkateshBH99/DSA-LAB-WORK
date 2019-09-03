class stack:
	def __init__(self):
		self.items=[]
		self.m=[]
		

	def push(self,val):
		self.items.append(val)
		if self.m==[]:
			self.m.append(val)
		elif self.m[len(self.m)-1]>val:
			self.m.append(val)

		
			
		

	def isEmpty(self):
		if self.items==[]:
			return True
		return False

	def pop(self):
		if self.isEmpty():
			return False
		if self.m[len(self.m)-1]==self.top():
			self.m.pop()
		return self.items.pop()

	def top(self):
		if self.isEmpty():
			return False
		return self.items[len(self.items)-1]

	def getMin(self):
		if self.isEmpty():
			return False
		return self.m[len(self.m)-1]

def main():
	S=stack()
	S.push(10)
	print(S.top(), S.getMin()) # Should print ‘10 10’
	S.push(12)
	print(S.top(), S.getMin()) # Should print ‘12 10’
	S.push(5)
	print(S.top(), S.getMin()) # Should print ‘5 5’
	S.push(3)
	print(S.top(), S.getMin()) # Should print ‘3 3’
	S.pop()
	S.pop()
	print(S.top(), S.getMin()) # Should print ‘12 10’
	S.pop()
	print(S.top(), S.getMin()) # Should print ‘10 10’


if __name__ == '__main__':
	main()
