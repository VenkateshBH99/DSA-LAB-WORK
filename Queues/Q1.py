class linked_list:
    def __init__(self):
        self.head=ListNode()
        self.tail=ListNode()
    
    def isEmpty(self):
        if self.head.next==None and self.tail.next==None:
            return True
        return False
    def enqueue(self,x):
        if self.isEmpty():
            temp=ListNode(x,self.tail.next)
            self.tail.next=temp
            self.head.next=self.tail.next
            return
        temp=ListNode(x,None)
        self.tail.next.next=temp
        self.tail.next=temp
        return
    def dequeue(self):
        if self.isEmpty():
            return print('List is empty!!')
        self.head.next=self.head.next.next
        if self.head.next==None:
            self.tail.next=None
        return
    def prin(self):
        if self.isEmpty():
            return print('List is Empty')
        l=self.head.next
        while l.next!=None:
            print(l.value)
            l=l.next
        #return print('\n')
        print(l.value)
        return


class ListNode:
    def __init__(self,val=None,nex=None):
        self.value=val
        self.next=nex
def main():
    s=linked_list()
    while True:
        ch=int(input('1.insert\n2.delete\n3.length\n4.print\n5.Exit\nEnter ur choice:'))
        if ch==1:
            x=input('Enter the value')
            s.enqueue(x)
        elif ch==2:
            s.dequeue()
        elif ch==3:
            print(s.len())
        elif ch==4:
            s.prin()
        elif ch==5:
            break
        else:
            print('Invalid choice!!')
    return
if __name__ == '__main__':
    main()
