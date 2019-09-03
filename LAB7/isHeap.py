
class BST:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

    def inorder(self,currNode):
        res=[]
        if currNode:
            res=self.inorder(currNode.left)
            res.append(currNode.val)
            res=res+self.inorder(currNode.right)
        return res

    def countNode(self,currNode):
        if currNode is None:
            return 0
        else:
            return (1+self.countNode(currNode.left)+self.countNode(currNode.right))

    def heap_propert_until(self,currNode):
        if (currNode.left is None and currNode.right is None):
            return True
        if currNode.right is None:
            return currNode.val >= currNode.left.val
        else:
            if (currNode.val >= currNode.left.val and currNode.val >=currNode.right.val):
                return (self.heap_propert_until(currNode.left) and self.heap_propert_until(currNode.right))
            else:
                return False

    def treeUtil(self,currNode,index,node):
        if currNode is None:
            return True
        if index >= node:
            return False
        return (self.treeUtil(currNode.left,2*index+1,node) and self.treeUtil(currNode.right,2*index+2,node))

    def isBinaryHeap(self):
        node=self.countNode(self)
        if (self.treeUtil(self,0,node) and self.heap_propert_until(self)):
            return True
        else:
            return False

def main():
    root=BST(5)
    root.left=BST(2)
    root.right=BST(3)
    root.left.left=BST(1)
    #root.right.right=BST(1)
    if root.isBinaryHeap():
        print('Given Binary Tree is Heap')
    else:
        print('Given Binary Tree is not Heap')
    print(root.inorder(root))


if __name__ == '__main__':
    main()
