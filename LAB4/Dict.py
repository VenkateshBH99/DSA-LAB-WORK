T=[None for i in range(30)]
x=33
class ListNode:
    def __init__(self,val=None,nex=None,k=None):
        self.value=val
        self.next=nex
        self.key=k


def asci(expr):
    l=len(expr)
    i=0
    sum=0
    while i!=l:
        sum=sum+ord(expr[i])
        i=i+1
    return sum
def insert(x):
    k=asci(x)%30
    if T[k]==None:
        T[k]=ListNode()
        temp=ListNode(x,T[k].next,k)
        T[k].next=temp
        return
    t=T[k].next
    while t.next!=None:
        t=t.next
    temp=ListNode(x,t.next,k)
    t.next=temp
    return
def sea(x):
    k=asci(x)%len(T)
    if T[k]==None:
        return print('value not found')
    t=T[k].next
    while t!=None:
        if t.value==x:
            return print(x,' found at key- ',k)
        t=t.next
    return

def large():
    fh=open("ispell.dict","r")
    l=fh.readlines()
    j=0
    while j!=len(l):
        insert(l[j])
        j=j+1

    i=len(l)-1
    str=asci(l[i])

    while i!=0:
        i=i-1
        str=asci(l[i])+(x*str)
    return str

def search(s,val):
    fh=open("ispell.dict","r")
    l=fh.readlines()

    c=asci(val)
    i=0
    while i-1!=len(l):
        i=i+1
        if (s-c)%x==0:
            print(val,' found at ',i)
        s=(s-asci(l[i-1]))
    return


def main():
    s=large()
    #search(s,'accent')
    str=input('enter')
    sea(str)


if __name__ == '__main__':
    main()
