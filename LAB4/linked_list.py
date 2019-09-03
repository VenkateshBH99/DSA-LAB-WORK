class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """
    
    def __init__(self):
        """Create a new list with a Sentinel Node"""
        self.head=ListNode()

    def insert(self,x,pos):
        """Insert element x in the position after pos"""
        l=ListNode(x,pos.next)
        pos.next=l
        return

    def delete(self,pos):
        """Delete the node following node pos in the linked list."""
        if pos.next!=None:
        	pos.next=pos.next.next
        else:
        	print("pos is last node")
        return

    def print(self):
        """ Print all the elements of a list in a row."""
        if(self.isEmpty()):
        	print("empty list")
        	return
        temp=self.head.next
        while temp.next!=None:
        	print(temp.value)
        	temp=temp.next
        print(temp.value)
        return


    def insertAtIndex(self,x,i):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        
        if i==0 :
        	l=ListNode(x,self.head.next)
        	self.head.next=l
        	return
        temp=self.head
        while temp.next!=None and i>0 : 
        	temp=temp.next
        	i=i-1
        self.insert(x,temp)
        return

    def search(self, x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        temp=self.head.next
        while temp.next!=None:
        	if(temp.value==x):
        		return temp
        	temp=temp.next
        if temp.value==x :
        	return temp
        return None

    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        temp=self.head
        c=0
        while temp.next != None:
        	temp=temp.next
        	c=c+1
        return c

    def isEmpty(self):
        """Return True if the Linked List has no elements, False otherwise."""
        if(self.len()==0):
        	return True
        return False


class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next. 
    """
    def __init__(self,val=None,nxt=None):
        self.value=val
        self.next=nxt

def main():
    L = LinkedList()
    L.insert(10,L.head)
    print('List is: ')
    L.print()
    L.insert(12,L.head.next)
    print('List is: ')
    L.print()
    L.insert(2,L.head)
    print('List is: ')
    L.print()
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is: ')
    L.print()
    L.delete(L.head.next)
    print('List is: ')
    L.print()
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.insertAtIndex(2,0)
    L.insertAtIndex(1,0)
    L.insertAtIndex(4,2)
    L.insertAtIndex(3,2)
    print('List is: ')
    L.print()
    print("6 is at ",L.search(6))
    print("3 is at ",L.search(3))

if __name__ == '__main__':
    main()
