from mystack import Stack
def operator(op):
    if op=='+'or op=='-'or op=='/'or op=='*'or op=='%':
        return True
    return False
def apply(a,b,op):
    if op=='+':
        return float(a)+float(b)
    elif op=='-':
        return float(a)-float(b)
    elif op=='*':
        return float(a)*float(b)
    elif op=='/':
        return float(a)/float(b)
    elif op=='%':
        return float(a)%float(b)
    else:
        return False
def convert(expr):
    S=Stack()
    sp=expr.split()
    l=len(sp)-1
    while l>=0:


        symb=sp[l]
        l=l-1
        if not operator(symb):
            S.push(symb)
        else:
            if S.isEmpty():
                return False
            else:
                a=S.pop()
                b=S.pop()
                c=a+" "+b+" "+symb
                S.push(c)
    return S.pop()
def eval_prefix(expr):
    T=Stack()
    sp=expr.split()
    l=len(sp)-1
    while l>=0:
        symb=sp[l]
        l=l-1
        if not operator(symb):
            T.push(symb)
        else:
            if T.isEmpty():
                return False
            else:
                a=T.pop()
                b=T.pop()
                c=apply(a,b,symb)
                T.push(c)
    return T.pop()




def main():
    expr = input('Enter the prefix expression: ')
    print('Conversion to postfix expression:',convert(expr))
    print('The value of the expression is',eval_prefix(expr))

if __name__ == '__main__':
    main()
