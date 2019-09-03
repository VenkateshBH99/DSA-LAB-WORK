class LinkedList:
	def __init__(self,val=None,nex=None):
		self.val=val
		self.next=nex

class Node:
	def __init__(self):
		self.head=None

	def insert(self,val):
		temp=LinkedList(val,self.head)
		self.head=temp

	def rev(self):
		pre=None
		curr=self.head
		while curr!=None:
			nex=curr.next
			curr.next=pre
			pre=curr
			curr=nex

		self.head=pre

	def prin(self):
		t=self.head
		while t!=None:
			print(t.val,end=' ')
			t=t.next
		print()

def main():
	l=Node()
	l.insert(2)
	l.insert(3)
	l.insert(4)
	l.insert(5)
	l.insert(6)
	l.insert(7)
	print('before rev:')
	l.prin()
	l.rev()
	print('after rev:')
	l.prin()

if __name__ == '__main__':
	main()