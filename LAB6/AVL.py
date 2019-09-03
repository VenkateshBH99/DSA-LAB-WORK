import time
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.rightChild=None
        self.leftChild=None
        self.count=1
        self.height=1

    def getChildren(self):
        child=[]
        if self.leftChild!=None:
            child.append(self.leftChild.val)
        if self.rightChild!=None:
            child.append(self.rightChild.val)
        return child
class AVL(object):

    def insertNode(self,currNode,val,m):
        if currNode==None:
            return TreeNode(val)
        elif val==currNode.val:
            if val==currNode.val:
                currNode.count+=1
                if currNode.count>m.ma:
                    m.ma=currNode.count
                    m.v=val
            return currNode
        elif val<currNode.val:
            currNode.leftChild=self.insertNode(currNode.leftChild,val,m)

        else:
            currNode.rightChild=self.insertNode(currNode.rightChild,val,m)

        currNode.height=1+max(self.getHeight(currNode.leftChild),self.getHeight(currNode.rightChild))
        balance=self.getBalance(currNode)

        #left left
        if balance > 1 and val <= currNode.leftChild.val:
            return self.rightRotate(currNode)

        #right right
        if balance < -1 and val > currNode.rightChild.val:
            return self.leftRotate(currNode)

        #left right
        if balance > 1 and val >currNode.leftChild.val:
            currNode.leftChild=self.leftRotate(currNode.leftChild)
            return self.rightRotate(currNode)

        #right left
        if balance < -1 and val <= currNode.rightChild.val:
            currNode.rightChild=self.rightRotate(currNode.rightChild)
            return self.leftRotate(currNode)
        return currNode

    def deleteNode(self,currNode,val):
        if currNode==None:
            return currNode
        elif val<currNode.val:
            currNode.leftChild=self.deleteNode(currNode.leftChild,val)
        elif val>currNode.val:
            currNode.rightChild=self.deleteNode(currNode.rightChild,val)
        else:
            #if it has one child or no child
            if currNode.leftChild==None:
                temp=currNode.rightChild
                currNode=None
                return temp
            elif currNode.rightChild==None:
                temp=currNode.leftChild
                currNode=None
                return temp
            #if it has two child
            temp=self.getMinNode(currNode.rightChild)
            currNode.val=temp.val
            #height sets
            currNode.rightChild=self.deleteNode(currNode.rightChild,temp.val)

        currNode.height=1+max(self.getHeight(currNode.leftChild),self.getHeight(currNode.rightChild))

        balance=self.getBalance(currNode)

        #left left
        if balance > 1 and self.getBalance(currNode.leftChild) >=0:
            return self.rightRotate(currNode)

        #right right
        if balance < -1 and self.getBalance(currNode.rightChild) <=0:
            return self.leftRotate(currNode)

        #left right
        if balance >1 and self.getBalance(currNode.leftChild) <0:
            currNode.leftChild=self.leftRotate(currNode.leftChild)
            return self.rightRotate(currNode)

        #right left
        if balance < -1 and self.getBalance(currNode.rightChild) >0:
            currNode.rightChild=self.rightRotate(currNode.rightChild)
            return self.leftRotate(currNode)

        return currNode


    def getHeight(self,currNode):
        if not currNode:
            return 0
        return currNode.height

    def getBalance(self,currNode):
        if not currNode:
            return 0
        return self.getHeight(currNode.leftChild)-self.getHeight(currNode.rightChild)

    def rightRotate(self,z):
        y=z.leftChild
        T3=y.rightChild
        #rotate
        y.rightChild=z
        z.leftChild=T3

        z.height=1+max(self.getHeight(z.leftChild),self.getHeight(z.rightChild))
        y.height=1+max(self.getHeight(y.leftChild),self.getHeight(y.rightChild))

        return y

    def leftRotate(self,z):
        y=z.rightChild
        T2=y.leftChild
        #rotate
        y.leftChild=z
        z.rightChild=T2

        z.height=1+max(self.getHeight(z.leftChild),self.getHeight(z.rightChild))
        y.height=1+max(self.getHeight(y.leftChild),self.getHeight(y.rightChild))

        return y

    def inorderNode(self,currNode):
        res=[]
        if currNode:
            res=self.inorderNode(currNode.leftChild)
            res.append(currNode.val)
            res=res+self.inorderNode(currNode.rightChild)
        return res

    def getMinNode(self,currNode):
        while currNode.leftChild:
            currNode=currNode.leftChild
        return currNode

    def getMaxNode(self,currNode):
        while currNode.rightChild:
            currNode=currNode.rightChild
        return currNode

    def preorder(self,currNode):
        res=[]
        if currNode:
            res.append(currNode.val)
            res=res+self.preorder(currNode.leftChild)
            res=res+self.preorder(currNode.rightChild)
        return res

    def postorder(self,currNode):
    	res=[]
    	if currNode:
    		res=self.postorder(currNode.leftChild)
    		res=res+self.postorder(currNode.rightChild)
    		res.append(currNode.val)

    def search(self,currNode,val):
        if currNode==None:
            return currNode
        elif val==currNode.val:
            return currNode
        elif val<currNode.val:
            return self.search(currNode.leftChild,val)
        else:
            return self.search(currNode.rightChild,val)

    def parent(self,currNode,val,res):
        if currNode==None:
            return False
        elif val==currNode.val:
            return res
        elif val<currNode.val:
            res=currNode
            return self.parent(currNode.leftChild,val,res)
        elif val>currNode.val:
            res=currNode
            return self.parent(currNode.rightChild,val,res)

    def predeccor(self,currNode,val):
        x=self.search(currNode,val)
        if x==None:
            return x
        if x.leftChild!=None:
            return self.getMaxNode(x.leftChild)
        y=self.parent(currNode,x.val,None)
        while y!=None and x==y.leftChild:
            x=y
            y=self.parent(currNode,y.val,None)
        return y

    def successor(self,currNode,val):
        x=self.search(currNode,val)
        if x==None:
            return None
        if x.rightChild!=None:
            return self.getMinNode(x.rightChild)
        y=self.parent(currNode,x.val,None)
        while y!=None and x==y.rightChild:
            x=y
            y=self.parent(currNode,y.val,None)
        return y

def main():
    l=AVL()
    root=None
    while True:
        ch=int(input("***AVL Tree***\n1.Insert\n2.Delete\n3.search\n4.inorder traversal\n5.preorder traversal\n6.minimum\n7.maximum\n8.predecessor\n9.successor\n10.getChildren\n11.Parent\n12.getHeight\n13.EXIT\nEnter ur Choice:"))
        if ch==1:
            a=int(input("Enter the value(Integer):"))
            root=l.insertNode(root,a)
        elif ch==2:
            a=int(input("Enter the value to be deleted:"))
            root=l.deleteNode(root,a)
        elif ch==3:
            a=int(input("Enter the value to be searched:"))
            p=l.search(root,a)
            if p!=None:
                print(p.val,' Found in the tree')
            else:
                print(a,' Not Found')
        elif ch==4:
            print(l.inorderNode(root))
        elif ch==5:
            print(l.preorder(root))
        elif ch==6:
            print(l.getMinNode(root).val)
        elif ch==7:
            print(l.getMaxNode(root).val)
        elif ch==8:
            a=int(input("Enter the value:"))
            p=l.predeccor(root,a)
            if p!=None:
                print('Predecessor of ',a,' is: ',p.val)
            else:
                print('there is no predecessor of ',a)
        elif ch==9:
            a=int(input("Enter the value:"))
            p=l.successor(root,a)
            if p!=None:
                print('successor of ',a,' is: ',p.val)
            else:
                print('there is no successor of ',a)
        elif ch==10:
            a=int(input('Enter the value:'))
            p=l.search(root,a)
            if p!=None:
                print(p.getChildren())
            else:
                print('Value does not exists')
        elif ch==11:
            a=int(input("Enter the value:"))
            p=l.parent(root,a,None)
            if p!=None and p!=False:
                print('parent:',p.val)
            elif p==False:
                print('entered value doesnt exits in Tree')
            else:
                print('entered value is root')
        elif ch==12:
            a=int(input('Enter the value to get Height:'))
            p=l.search(root,a)
            if p!=None:
                print('Height:',p.height)
            else:
                print('value does not exists')
        elif ch==13:
            break
        else:
            print('INVALID CHOICE!!')

    """root=l.insertNode(root,10)
    root=l.insertNode(root,20)
    root=l.insertNode(root,30)
    root=l.insertNode(root,40)
    root=l.insertNode(root,50)
    root=l.insertNode(root,25)
    print(l.inorderNode(root))
    print(l.preorder(root))
    print(l.successor(root,25).val)
    print(l.successor(root,30).val)
    print(l.predeccor(root,30).val)
    root=l.deleteNode(root,30)
    root=l.deleteNode(root,40)
    root=l.deleteNode(root,20)
    root=l.deleteNode(root,10)
    root=l.deleteNode(root,25)
    root=l.deleteNode(root,5)
    print(l.inorderNode(root))"""

if __name__ == '__main__':

    main()

