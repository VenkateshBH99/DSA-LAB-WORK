class Vertices:
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

    def BFS(self,s):
        V=[Vertices() for i in range(len(self.graph))]
        V[s].dist=0
        V[s].color="grey"
        queue=[]
        queue.append(s)
        while queue:
            s=queue.pop(0)
            for i in self.graph[s]:
                i=int(i)
                if V[i].color=="grey":
                    return True
                elif V[i].color=="white":
                    V[i].color="grey"
                    V[i].dist=V[s].dist
                    V[i].parent=V[s]
                    queue.append(i)
            V[s].color="black"
        return False

def main():
    n=int(input("Enter the number of vertices:"))
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

    s=int(input('Enter the source vertex:'))
    cy=g.BFS(s)
    if cy==True:
        print('Entered graph has a cycle')
    else:
        print('Entered graph does not has cycle')
if __name__ == '__main__':
    main()
