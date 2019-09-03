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

    def BFS(self,s):
        V=[Vertex() for i in range(len(self.graph))]
        V[s].dist=0
        V[s].color="grey"
        queue=[]
        queue.append(s)
        while queue:
            s=queue.pop(0)
            print('vertex:',s,', distance:',V[s].dist)
            for i in self.graph[s]:
                i=int(i)
                if V[i].color=="white":
                    V[i].color="grey"
                    V[i].dist=V[s].dist+1
                    V[i].parent=V[s]
                    queue.append(i)
            V[s].color="black"

        return V


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
    print("Following is BST from source vertex ",s," :")
    l=g.BFS(s)


    """ed=input("Enter the edges:")
    l=ed.split(' ')
    for i in range(len(l)):
        #print(l[i])
        d=list(l[i])
        n1=int(d[0])
        n2=int(d[1])
        if n1>=n or n2>=n:
            return print(n1,' or ',n2,' cannot be more than ',n-1)
        g.addEdge(n1,n2)
    s=int(input('Enter the source vertex:'))
    print("Following is BST from source vertex ",s," :")
    l=g.BFS(s)"""

    """g.addEdge(0,1)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,4)
    g.addEdge(3,5)
    g.addEdge(4,5)
    g.addEdge(4,6)
    g.addEdge(4,7)
    g.addEdge(5,6)
    g.addEdge(6,7)
    print("Following:")
    l=g.BFS(3)"""



if __name__ == '__main__':
    main()







