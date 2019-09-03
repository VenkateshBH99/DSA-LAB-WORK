from array import *
V=[]
E=[]
M=[]
class ListNode:
	def __init__(self,val=None,nex=None):
		self.val=val
		self.next=nex


def mat(M,n1,n2,n):
	if (n1>=n or n2>=n):
		return print(n2,' or ',n1,' cannot be more than ',n-1)
	M[n1][n2]=1
	M[n2][n1]=1
	return M

def prinM(M):
	print('\nThe adjacency matrix is:')
	for i in M:
		for c in i:
			print(c,end=' ')
		print()
	return
"""def adinsert(V,n):
	for i in range(len(E)):
		n1=int(E[i])%10
		n2=int(E[i])//10
		if (n1>=n or n2>=n):
			return False
		if V[n1]==None:
			V[n1]=ListNode()
			t=ListNode(n2,None)
			V[n1].next=t
		elif V[n1]!=None:
			l=V[n1].next
			while l.next!=None:
				l=l.next
			t=ListNode(n2,None)
			l.next=t
		if V[n2]==None:
			V[n2]=ListNode()
			t=ListNode(n1,None)
			V[n2].next=t
		elif V[n2]!=None:
			l=V[n2].next
			while l.next!=None:
				l=l.next
			t=ListNode(n1,None)
			l.next=t

	print('\nThe adjacency list is:')
	for i in range(len(V)):
		if V[i]!=None:
			l=V[i].next
			print('Vertex',i,':',end='')
			while l!=None:
				print(l.val,end=',')
				l=l.next
			print('\n')
	return"""

def ainsert(V,n1,n2,n):
	if (n1>=n or n2>=n):
		return False
	if V[n1]==None:
		V[n1]=ListNode()
		t=ListNode(n2,None)
		V[n1].next=t
	elif V[n1]!=None:
		l=V[n1].next
		while l.next!=None:
			l=l.next
		t=ListNode(n2,None)
		l.next=t
	if V[n2]==None:
		V[n2]=ListNode()
		t=ListNode(n1,None)
		V[n2].next=t
	elif V[n2]!=None:
		l=V[n2].next
		while l.next!=None:
			l=l.next
		t=ListNode(n1,None)
		l.next=t

	return V

def prinL(V):
	print('\nThe adjacency list is:')
	for i in range(len(V)):
		if V[i]!=None:
			l=V[i].next
			print('Vertex',i,':',end='')
			while l!=None:
				print(l.val,end=',')
				l=l.next
			print('\n')

def main():
	n=int(input("Enter the number of vertices:"))
	V=[None for i in range(n)]
	M=[[0 for j in range(n)] for i in range(n)]
	while True:
		ch=input("want to add edge? for Yes[y/Y],for No[any other key]:")
		if ch=="y" or ch=="Y":
			ed=input("Enter edge:")
			d=ed.split()
			V=ainsert(V,int(d[0]),int(d[1]),n)
			M=mat(M,int(d[0]),int(d[1]),n)
		else:
			break
	prinM(M)
	prinL(V)
	"""va=input("Enter the edges:")
	l=va.split(' ')
	for i in l:
		E.append(i)
	matrix(M,n)
	adinsert(V,n)"""


if __name__ == '__main__':
	main()

