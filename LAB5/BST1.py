class TreeNode:
    def __init__(self,val):
        self.val=val
        self.leftChild=None
        self.rightChild=None

    def get(self):
        return self.val
    def set(self,val):
        self.val=val
    def getChildren(self):
        children=[]
        if self.leftChild!=None:
            children.append(self.leftChild.val)
        if self.rightChild!=None:
            children.append(self.rightChild.val)
        return children

class BST:
    def __init__(self):
        self.root=None

    def setRoot(self,val):
        self.root=TreeNode(val)

    def insert(self,val):
        if self.root==None:
            self.setRoot(val)
        else:
            self.insertNode(self.root,val)

    def insertNode(self,currNode,val):
        if val<=currNode.val:
            if currNode.leftChild:
                self.insertNode(currNode.leftChild,val)
            else:
                currNode.leftChild=TreeNode(val)
        elif val>currNode.val:
            if currNode.rightChild:
                self.insertNode(currNode.rightChild,val)
            else:
                currNode.rightChild=TreeNode(val)

    def search(self,val):
        return self.searchNode(self.root,val)

    def searchNode(self,currNode,val):
        if currNode==None:
            return currNode
        elif val==currNode.val:
            return currNode
        elif val<currNode.val:
            return self.searchNode(currNode.leftChild,val)
        else:
            return self.searchNode(currNode.rightChild,val)

    def inorder(self):
        return self.inorderNode(self.root)

    def inorderNode(self,currNode):
        res=[]
        if currNode:
            res=self.inorderNode(currNode.leftChild)
            res.append(currNode.val)
            res=res+self.inorderNode(currNode.rightChild)
        return res

    def max(self):
        res=None
        return self.maxNode(self.root,res)
    def maxNode(self,currNode,res):
        if currNode:
            res=currNode
            return self.maxNode(currNode.rightChild,res)
        return res
    def min(self):
        res=None
        return self.minNode(self.root,res)
    def minNode(self,currNode,res):
        if currNode:
            res=currNode
            return self.minNode(currNode.leftChild,res)
        return res
    def parent(self,val):
        res=None
        return self.parentNode(self.root,val,res)
    def parentNode(self,currNode,val,res):
        if currNode==None:
            return False
        elif val==currNode.val:
            return res
        elif val<currNode.val:
            res=currNode
            return self.parentNode(currNode.leftChild,val,res)
        elif val>currNode.val:
            res=currNode
            return self.parentNode(currNode.rightChild,val,res)

    def predeccor(self,z):
        x=self.search(z)
        if x.leftChild!=None:
            res=z
            return self.maxNode(x.leftChild,res)
        y=self.parent(x.val)
        while y!=None and x==y.leftChild:
            x=y
            y=self.parent(y.val)
        return y

    def successor(self,z):
        x=self.search(z)
        if x.rightChild!=None:
            res=z
            return self.minNode(x.rightChild,res)
        y=self.parent(x.val)
        while y!=None and x==y.rightChild:
            x=y
            y=self.parent(y.val)
        return y

    def delete(self,s):
        z=self.search(s)
        if z.leftChild==None or z.rightChild==None:
            y=z
        else:
            y=self.successor(s)
        if y.leftChild!=None:
            x=y.leftChild
        else:
            x=y.rightChild
        if x!=None:
            t=self.parent(x.val)
            q=self.parent(y.val)
            t=q
        if self.parent(y.val)==None:
            self.root=x
        else:
            if y==self.parent(y.val).leftChild:
                self.parent(y.val).leftChild=x
            else:
                self.parent(y.val).rightChild=x
        if y!=z:
            z.val=y.val
        return



def main():
    l=BST()
    while True:
        ch=int(input("1.insert\n2.delete\n3.search\n4.inorder traversal\n5.getChildern\n6.minimum\n7.maximum\n8.predecessor\n9.successor\n10.parent\n11.EXIT\n Enter ur choice:"))
        if ch==1:
            a=int(input("Enter the value(integer):"))
            l.insert(a)
        elif ch==2:
            a=int(input("Enter the value to be deleted:"))
            l.delete(a)
        elif ch==3:
            a=int(input("Enter the value to be searched:"))
            p=l.search(a)
            if p!=None:
                print(p.val,' Found in the tree')
            else:
                print('Not Found')
        elif ch==4:
            print(l.inorder())
        elif ch==5:
            a=int(input("Enter the parent value to get Childern:"))
            p=l.search(a)
            if p!=None:
                print(p.getChildren())
            else:
                print('Value does no exits')
        elif ch==6:
            print(l.min().val)
        elif ch==7:
            print(l.max().val)
        elif ch==8:
            a=int(input("Enter the value:"))
            p=l.predeccor(a)
            if p!=None:
                print(p.val)
            else:
                print('Theres No predecessor')
        elif ch==9:
            a=int(input("Enter the value:"))
            p=l.successor(a)
            if p!=None:
                print(p.val)
            else:
                print('Theres no successor')
        elif ch==10:
            a=int(input("Enter the Child value:"))
            p=l.parent(a)
            if p!=None:
                print(p.val)
            else:
                print('entered value is root')
        elif ch==11:
            break
        else:
            print("Invalid Choice")

    """l.insert(5)
    l.insert(2)
    l.insert(3)
    l.insert(4)
    l.insert(5)
    l.insert(6)
    l.insert(2)
    l.insert(1)
    l.insert(7)
    l.insert(12)
    p=l.search(21)
    if p!=None:
        print(p.val,' found in the tree')
    else:
        print('Not found')
    print(l.inorder())
    print(l.root.getChildren())

    print(l.min().val)
    print(l.max().val)
    print(l.predeccor(7).val)
    print(l.successor(6).val)
    l.delete(7)
    print(l.inorder())"""

if __name__ == '__main__':
    main()
