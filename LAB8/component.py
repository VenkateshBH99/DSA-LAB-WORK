class Vertex:
    def __init__(self,dist="infinite",color="white",parent=None):
        self.dist=dist
        self.color=color
        self.parent=parent

class Graph:
    def __init__(self,n):
        self.graph=[[] for i in range(n)]

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BFS(self,E,s,j):
        V=[Vertex() for i in range(len(self.graph))]
        V[s].dist=0
        V[s].color="grey"
        queue=[]
        queue.append(s)
        while queue:
            s=queue.pop(0)
            print('Vertex:',s,', distance:',V[s].dist)
            E[s]=j
            for i in self.graph[s]:
                i=int(i)
                if V[i].color=="white":
                    V[i].color="grey"
                    V[i].dist=V[s].dist+1
                    V[i].parent=V[s]
                    queue.append(i)
            V[s].color="black"
        return E


def main():
    n=int(input("Enter number of vertices:"))
    E=[0 for i in range(n)]
    g=Graph(n)
    while True:
        ed=input("for Stop[press s]/Enter edge::")
        if ed=="s":
            break
        d=ed.split(' ')
        n1=int(d[0])
        n2=int(d[1])
        if n1>=n or n2>=n:
            print(n1,' or ',n2,' cannot be more than ',n-1)
        else:
            g.addEdge(n1,n2)

    j=1
    for i in range(len(E)):
        if E[i]==0:
            print('------------------------------')
            print('Component:',j,', source vertex:',i)
            E=g.BFS(E,i,j)
            j=j+1



if __name__ == '__main__':
    main()
