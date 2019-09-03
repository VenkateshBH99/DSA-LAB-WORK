from Stack import Stack
from matchsym import isMatched
class BST:
    def __init__(self,val=None):
        self.val=val
        self.rigthChild=None
        self.leftChild=None

    def insertLeft(self,x):
        self.leftChild=BST(x)
    def getLeftChild(self):
        return self.leftChild
    def insertRight(self,x):
        self.rigthChild=BST(x)
    def getRightChild(self):
        return self.rigthChild
    def setRootVal(self,x):
        self.val=x
    def postorder(self,currentNode):
        if currentNode:
            self.postorder(currentNode.leftChild)
            self.postorder(currentNode.rigthChild)
            print(currentNode.val,end=' ')

    def preorder(self,currenNode):
        if currenNode:
            print(currenNode.val,end=' ')
            self.preorder(currenNode.leftChild)
            self.preorder(currenNode.rigthChild)

def evaluateTree(root):
    if root is None:
        return 0
    if root.leftChild is None and root.rigthChild is None:
        return int(root.val)
    leftsum = evaluateTree(root.leftChild)
    rightsum = evaluateTree(root.rigthChild)
    if root.val=='+':
        return leftsum + rightsum
    elif root.val=='-':
        return leftsum - rightsum
    elif root.val=='*':
        return leftsum * rightsum
    else:
        return leftsum / rightsum

def ParseTree(exp):
    list=exp.split()
    S= Stack()
    Tree = BST('')
    S.push(Tree)
    current=Tree
    for i in list:
        if i=='(':
            current.insertLeft('')
            S.push(current)
            current=current.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            current.setRootVal(int(i))
            parent=S.pop()
            current=parent
        elif i in ['+', '-', '*', '/']:
            current.setRootVal(i)
            current.insertRight('')
            S.push(current)
            current=current.getRightChild()
        elif i==')':
            current=S.pop()
        else:
            raise ValueError
    return Tree

def main():
    expr=input('Enter the valid fully parenthesised expression:')
    if not isMatched(expr):
        return print('invalid input')
    pt=ParseTree(expr)
    print('postorder:',end=' ')
    pt.postorder(pt)
    print()
    print('preorder:',end=' ')
    pt.preorder(pt)
    print()
    print('evaluation:',evaluateTree(pt))
    
if __name__ == '__main__':
    main()
