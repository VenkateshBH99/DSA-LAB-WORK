class ArrayQueue:
    def __init__(self,T=[None for i in range(10)],fro=-1,rea=-1):
        self.elements=T
        self.front=fro
        self.rear=rea
class Array:
    def __init__(self):
        self.Q=ArrayQueue()

    def isEmpty(self):
        if self.Q.front==-1 and self.Q.rear==-1:
            return True
        return False

    def isFull(self):
        if self.Q.front==(self.Q.rear+1)%len(self.Q.elements):
            return True
        return False


    def enqueue(self,x):
        if self.isFull():
            return print('Queue is Full,Cannot enqueue')
        if self.isEmpty():
            self.Q.front=0
        t=self.Q
        t.rear=(t.rear+1)%len(t.elements)
        t.elements[t.rear]=x
        return
    def dequeue(self):
        if self.isEmpty():
            return print('There are no elements to remove')
        f=self.Q.elements[self.Q.front]
        #Only 1 element left in Queue
        if self.Q.front==self.Q.rear:
            self.Q.front,self.Q.rear=-1,-1
            return
        self.Q.front=(self.Q.front+1)%len(self.Q.elements)
        return f

    def prin(self):
        if self.isEmpty():
            return print('Queue is Empty')
        temp=ArrayQueue(self.Q.elements,self.Q.front,self.Q.rear)
        while temp.front!=temp.rear:
            print(temp.elements[temp.front])
            temp.front=(temp.front+1)%len(temp.elements)
        print(temp.elements[temp.front])
        return

def main():
    l=Array()
    while True:
        ch=int(input('1.enqueue\n2.dequeue\n3.print\n4.Exit\nEnter ur Choice:\n'))
        if ch==1:
            x=input('Enter the value')
            l.enqueue(x)
        elif ch==2:
            l.dequeue()
        elif ch==3:
            l.prin()
        elif ch==4:
            break
        else:
            print('Enter valid choice')
    return

if __name__ == '__main__':
    main()










