from mystack import Stack
def match(x,y):
    if x==')' and y=='(':
        return True
    elif x=='}' and y=='{':
        return True
    elif x==']'and y=='[':
        return True
    return False

def isMatched(expr):
    """Checks if the expression 'expr' has matching opening/closing symbols."""
    sp=expr.split()
    
    b=0
    S=Stack()
    
    while b!=len(sp):
        symb=sp[b]
        b=b+1
        if symb=='{' or symb=='[' or symb=='(':
            t=symb
            S.push(symb)
    
        elif symb=='}' or symb==']' or symb==')':
            if S.isEmpty():
                return False
            else:
                left=S.pop()
                
                if not match(symb,left):
                    return False
        
    return S.isEmpty()

def HasHigherPre(a,b):
    t=0
    if a=='+' or a=='-':
        if b=='+' or b=='-':
            t=1

    if a=='*' or a=='/' or a=='%':
        if b=='*' or b=='/' or a=='%':
            t=1
    
    if a=='*' or a=='/' or a=='%':
        if b=='+' or b=='-':
            t=1

    if t is not 0:
        return True
    else:
        return False
def OpeningPara(a):
    if a=='(' or a=='{' or a=='[':
        return True
    return  False
def ClosingPara(a):
    if a==')' or a=='}' or a==']':
        return True
    return  False
def operand(a):
    return a.isalpha() or a.isdigit()
def operator(a):
    if a=='+' or a=='-' or a=='/' or a=='*' or a=='%':
        return  True
    return False
def infixTOPost(expr):
    S=Stack()
    
    sp=expr.split()
    i=0
    res=''
    while i!=len(sp):
        symb=sp[i]
        i=i+1
        if operand(symb):
            res=res+' '+symb
        elif operator(symb):
            while not S.isEmpty() and not OpeningPara(S.top()) and HasHigherPre(S.top(),symb):
                res=res+' '+S.top()
                S.pop()
            S.push(symb)
        elif OpeningPara(symb):
            S.push(symb)
        elif ClosingPara(symb):
            while not S.isEmpty() and not OpeningPara(S.top()):
                res=res+' '+S.top()
                S.pop()
            S.pop()

    while not S.isEmpty():
        res=res+' '+S.top()
        S.pop()
    return res
def main():
    
    expr=input('Enter the infix expression: ')
    if not isMatched(expr):
        print('Un-Matched symbols')
    
    else:
        if expr=='':
            print('expression is empty')
        else:
            print('postfix expression is :',infixTOPost(expr))
if __name__=='__main__':
    main()

