from Heap import Heap
def heapsort(l,alist):
    for i in range(len(alist)-1,1,-1):
        if alist[1] > alist[i]:
            alist[1],alist[i]=alist[i],alist[1]
            moveDown(l.items,1,i-1)

def moveDown(alist,i,last):
    largest=2*i
    while largest<=last:
        #right child exists and is larger than left child
        if (largest<last) and (alist[largest] < alist[largest+1]):
            largest +=1

        #right/left child is larger than parent
        if alist[largest] > alist[i]:
            alist[largest],alist[i]=alist[i],alist[largest]
            i=largest
            largest=2*i
        else:
            return




def main():
    alist=[3,2,5,6,9]
    l=Heap()
    l.build_heap(alist)
    while True:
        ch=int(input("1.insert\n2.max_child\n3.exract_max\n4.print\n5.Heapify\n6.Heapsort\n7.Exit\nEnter ur choice:"))
        if ch==1:
            a=int(input("Entre the value:"))
            l.insert(a)
        elif ch==2:
            a=int(input("Enter the index:"))
            print(l.items[l.maximum(a)])
        elif ch==3:
            print(l.extract_Max())
        elif ch==4:
            print(l.prin())
        elif ch==5:
            l.heapify()
        elif ch==6:
            heapsort(l,l.items)
        elif ch==7:
            break
        else:
            print('Invalid choice')
if __name__ == '__main__':
    main()

