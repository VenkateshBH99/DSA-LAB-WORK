k=int(input("enter the value in integer"))



def strobo(n):
 result=num(n,n)
 return result



def num(n,l):
    if n==0: return [""]
    if n==1: return ["1","0","8"]
    middle=num(n-2,l)
    result=[]
    for i in middle:
        if n!=l:
         result.append("0"+i+"0")

        result.append("1"+i+"1")
        result.append("6"+i+"9")
        result.append("8"+i+"8")
        result.append("9"+i+"6")

    return result

if __name__=='__main__':
   print(strobo(k))