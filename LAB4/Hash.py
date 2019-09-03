T = [None for i in range(30)]

def ascii(value):
    l=len(value)
    i=0
    sum=0
    while i!=l:
        sum=sum+ord(value[i])
        i=i+1
    return sum

def insert(T,value):
    key=ascii(value)%len(T)


    if T[key]==None:
        T[key]=ListNode()
        temp=ListNode(key,value,T[key].next)
        T[key].next=temp
        return

    l=T[key].next
    while l.next!=None:
        l=l.next
    temp=ListNode(key,value,l.next)
    l.next=temp
    return

def search(T,val):
    key=ascii(val)%len(T)
    if T[key]==None:
        return print('value not found ')
    l=T[key].next
    while l!=None:
        if l.value==val:
            return l
        l=l.next
    return False

def T_print(T):
    i=0
    while i!=len(T):
        if T[i]!=None:
            print(i)
        i=i+1
    return

def print_all(T):
    for i in range(0,len(T)):
        if T[i]!=None:
            temp=T[i].next
            print('key',i,'-',end=' ')
            while temp!=None:
                print(temp.value,end=',')
                temp=temp.next
            print("\n")
    return



class ListNode:
	def __init__(self,k=None,val=None,nex=None):
		self.key=k
		self.value=val
		self.next=nex

def main():
    while True:
        ch=int(input("Enter\n1 for inserting\n2 for searching\n3 for printing key values\n4 for printing all values\n5 exit \n"))
        if ch==1:
            inp=input("Enter the input")
            insert(T,inp)
        elif ch==2:
            value=input('enter the value to search:')
            print(value,' found at : ',search(T,value),' in key:',ascii(value)%len(T))
        elif ch==3:
            T_print(T)
        elif ch==4:
            print_all(T)
        elif ch==5:
            break
        else:
            print("Invalid choice")


if __name__=='__main__':
	main()



