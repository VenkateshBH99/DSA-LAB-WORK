class adjnode:
	def __init__(self,data):
		self.vertex=data
		self.next=None
class Graph:
	def __init__(self,vertices):
		self.v=vertices
		self.graph=[None for i in range(self.v)]#[None]*self.v
	def addedge(self,src,dest):
		node = adjnode(dest)
		node.next=self.graph[src]
		self.graph[src]=node
		node=adjnode(src)
		node.next=self.graph[dest]
		self.graph[dest]=node
	def print(self):
		print("Adjecency list:")
		for i in range(self.v):
			if (self.graph[i]!=None):
				t = self.graph[i]
				print('vertex:',i,'-',end='')
				while t!=None: 
					print(t.vertex,end=',')
					t=t.next
				print()
def matrix(m,n1,n2):
	m[n1][n2]=1
	m[n2][n1]=1
	return m
def printm(m):
    print('adjancey matrix:')
    for i in range(len(m)):
    	for j in range(len(m)):
    		print(m[i][j],end=" ")

    	print()



def main():

	n=int(input("enter the number of vertices:"))
	m=[[0 for j in range(n)] for i in range(n) ]

	g=Graph(n)
	while True:
		ch=input("want to enter edge? for yes[y/Y],for No[any key]:")
		if ch=="y" or ch=="Y":
			ed=input("Enter edge:")
			d=ed.split(' ')
			n1=int(d[0])
			n2=int(d[1])
			g.addedge(n1,n2)
			m=matrix(m,n1,n2)
		else:
			break
	printm(m)
	g.print()

if __name__ == '__main__':
	main()
