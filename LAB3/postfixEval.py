from mystack import Stack
def operator(op):
    if op=='+'or op=='-'or op=='/'or op=='*'or op=='%':
        return True
    return False
def apply(op,a,b):
    if op=='+':
        return float(b)+float(a)
    elif op=='-':
        return float(b)-float(a)
    elif op=='*':
        return float(b)*float(a)
    elif op=='/':
        return float(b)/float(a)
    elif op=='%':
        return float(b)%float(a)
    else:
        return False
def eval_postfix(s):
    """Evaluates the postfix expression 's'."""
    S=Stack()
    l=s.split(' ')
    i=0
    while i!=len(l):
        symb=l[i]
        i=i+1
        if not operator(symb):
            S.push(symb)
        else:
            a=S.pop()
            b=S.pop()
            result=apply(symb,a,b)
            S.push(result)
    return S.pop()


def main():
    expr = input('Enter the postfix expression: ')
    print('The value of the expression is',eval_postfix(expr))

if __name__ == '__main__':
    main()

