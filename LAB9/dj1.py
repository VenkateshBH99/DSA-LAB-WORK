from Heap3 import Heap2


class vertex:
	def __init__(self,ui=None,dist=float("infinity"),parent=None):
		self.ui=int(ui)
		self.dist=dist
		self.parent=parent

class weigth:
	def __init__(self,u=None,v=None,wi=0):
		self.v=v
		self.wi=wi
		self.u=u

class Graph:
	def __init__(self,n):
		self.graph=[[] for i in range(n)]
		self.V=[]
		for i in range(n):
			self.V.append(vertex(i,float("infinity"),None))

	def addEdge(self,u,v,wi):
		self.graph[u].append(weigth(u,v,wi))

	def dijkstra(self,s,d):
		#V=[vertex() for i in range(len(self.graph)) ]
		self.V[s].dist=0
		H=Heap2()
		for i in range(len(self.V)):
			H.insert([self.V[i],self.V[i].dist])

		#w=H.extract_Min()
		#print(w.ui)


		while H.isEmpty()!=True:
			w=H.extract_Min()
			for i in self.graph[w.ui]:
				if self.V[i.v].dist > (w.dist+i.wi):
					self.V[i.v].dist=w.dist+i.wi
					H.updatePriority(self.V[i.v],self.V[i.v].dist)
					self.V[i.v].parent=w

		q=[]
		q.append(d)
		t=self.V[d].parent
		while t!=None:
			q.append(t.ui)
			t=t.parent
		return q


	def prin(self):
		for i in range(len(self.V)):
			print('Vertex:',i,' dist:',self.V[i].dist,' parent:',end='-')
			t=self.V[i].parent
			while t!=None:
				print(t.ui,end='<')
				t=t.parent
			print()


def main():
	n=int(input("Enter the number of vertices:"))
	g=Graph(n)
	while True:
		ed=input("For Stop[press s]/Enter edge:")
		if ed=="s":
			break

		d=ed.split(' ')
		u=int(d[0])
		v=int(d[1])
		if u>=n or v>=n:
			print(u,' or ',v,' cannot be more than ',n-1)
			continue
		wi=int(input("Enter dist "))
		g.addEdge(u,v,wi)

	s=int(input("Enter source vertex:"))
	t=int(input("Enter destination:"))
	print('following:')
	print(g.dijkstra(s,t))
	g.prin()


if __name__ == '__main__':
    main()
