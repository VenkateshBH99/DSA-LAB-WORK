elements=[None for i in range(10)]
class Array:
    def __init__(self,fro=-1,rea=-1):
        self.front=fro
        self.rear=rea

    def isEmpty(self):
        if self.front==-1 and self.rear==-1:
            return True
        return False

    def isFull(self):
        if self.front==(self.rear+1)%len(elements):
            return True
        return False

    def enqueue(self,x):
        if self.isFull():
            return print('Queue is Full,Cannot enqueue')
        if self.isEmpty():
            self.front=0
        
        self.rear=(self.rear+1)%len(elements)
        elements[self.rear]=x
        return

    def dequeue(self):
        if self.isEmpty():
            return print('There are no elements to remove')
        f=elements[self.front]
        #Only 1 element left in Queue
        if self.front==self.rear:
            self.front,self.rear=-1,-1
            return
        self.front=(self.front+1)%len(elements)
        return f

    def prin(self):
        if self.isEmpty():
            return print('Queue is Empty')
        temp=Array(self.front,self.rear)
        while temp.front!=temp.rear:
            print(elements[temp.front])
            temp.front=(temp.front+1)%len(elements)
        print(elements[temp.front])
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










