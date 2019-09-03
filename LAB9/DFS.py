class vertex:
	def __init__(self,color="white",t1=0,t2=0,parent=None):
		self.color=color
		self.t1=t1
		self.t2=t2
		self.parent=parent


class Graph:
	def __init__(self,n):
		self.graph=[[] for i in range(n)]
		self.V=[vertex() for i in range(n)]
		self.time=-1


	def addedge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def DFS(self,s):
		self.V[s].color="grey"
		

		print(s,end=' ')
		self.time=self.time+1
		self.V[s].t1=self.time
		for i in self.graph[s]:
			if self.V[i].color=="white":
				self.DFS(i)
		self.time=self.time+1
		self.V[s].t2=self.time


	def sor(self):
		for i in self.graph:
			i.sort()

	def prin(self):
		for i in range(len(self.V)):
			if self.V[i].color=="grey":
				print('Vertex:',i,' timestamps:[',self.V[i].t1,',',self.V[i].t2,']')




def main():
	n=int(input("Enter the number of Vertices:"))
	g=Graph(n)
	
	while True:
		ed=input("for Stop[press s]/Enter edge:")
		if ed=="s":
			break
		d=ed.split(' ')
		u=int(d[0])
		v=int(d[1])
		if u>=n or v>=n:
			print(u,' or ',v,' cannot be more than ',n-1)
			continue
		g.addedge(u,v)

	s=int(input('Enter the source vertex:'))
	print("Following is DFS from source vertex ",s,":")
	g.sor()

	g.DFS(s)
	print("\nTimeStamps of each vertex:")
	g.prin()


if __name__ == '__main__':
	main()
