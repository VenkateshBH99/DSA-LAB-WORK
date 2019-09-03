from mystack import Stack
def match(x,y):
 if y==')' and x=='(':
         return True
 elif y=='}' and x=='{':
    	return True
 elif y==']'and x=='[':
    	return True
 return False

def isMatched(expr):
    """Checks if the expression 'expr' has matching opening/closing symbols."""
    #a=list(expr)
    #print(a)
    #b=0
    S=Stack()
    l=len(expr)
    i=0
    while i!=l:
      symb=expr[i]
      i=i+1
      
      if symb=='{' or symb=='[' or symb=='(':
      	t=symb
      	S.push(symb)
      
      elif symb=='}' or symb==']' or symb==')':
       if S.isEmpty():
      	    return False
       else:
      	   left=S.pop()
       if not match(left,symb):
         return False
                 
      

    if S.isEmpty():
    	return True
    else:
    	return False
        

    	
    
    
def main():
	expr = input('Enter the expression: ')
	
	if isMatched(expr):
		print('Matched symbols')
	else:
		print('Unmatched symbols')

if __name__ == '__main__':
    main()

