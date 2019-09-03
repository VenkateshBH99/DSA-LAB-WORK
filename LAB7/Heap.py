class Heap:
    def __init__(self):
        self.items=[0]
    def __len__(self):
        return len(self.items)-1

    def insert(self,val):
        self.items.append(val)
        self.up()

    def up(self):
        i=len(self)
        while i//2 > 0:
            if self.items[i]>self.items[i//2]:
                self.items[i],self.items[i//2]=self.items[i//2],self.items[i]
            i=i//2

    def extract_Max(self):
        if len(self)==1:
            return str('cannot extract_Max no elements present')
        value=self.items[1]
        self.items[1]=self.items[len(self)]
        self.items.pop()
        self.down(1)
        return value

    def down(self,i):
        while 2*i<=len(self):
            mc=self.maximum(i)
            if self.items[i]<self.items[mc]:
                self.items[i],self.items[mc]=self.items[mc],self.items[i]
            i=mc
    def maximum(self,i):
        if 2*i+1 > len(self):
            return 2*i
        if self.items[2*i] > self.items[2*i+1]:
            return 2*i
        return 2*i+1

    def build_heap(self,alist):
        i=len(alist)//2
        self.items=[0]+alist
        while i>0:
            self.down(i)
            i=i-1
    def prin(self):
        res=[]
        for i in range(1,(len(self.items))):
            res.append(self.items[i])
        return res

    def heapify(self):
        i=len(self)//2
        while i>0:
            self.down(i)
            i=i-1


def main():
    alist=[3,2,5,6,9]
    l=Heap()
    l.build_heap(alist)
    while True:
        ch=int(input("1.insert\n2.max_child\n3.exract_max\n4.print\n5.Heapify\n6.Exit\nEnter ur choice:"))
        if ch==1:
            a=int(input("Entre the value:"))
            l.insert(a)
        elif ch==2:
            a=int(input("Enter the index:"))
            print(l.items[l.maximum(a)])
        elif ch==3:
            l.extract_Max()
        elif ch==4:
            print(l.prin())
        elif ch==5:
            l.heapify()
        elif ch==6:
            break
        else:
            print('Invalid choice')
if __name__ == '__main__':
    main()






