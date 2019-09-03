class Fraction:
    
    def __init__(self,top,bottom):
        self.num=top
        self.den=bottom
    
    def inverse(self):
        return Fraction(self.den,self.num)
        pass
    
    def add(self,f):
        num1=self.num*f.den+f.num*self.den
        den1=self.den*f.den
        return Fraction(num1,den1)
        pass
    
    def sub(self,f):
        num1=self.num*f.den-f.num*self.den
        den1=self.den*f.den
        return Fraction(num1,den1)
        pass
    
    def mul(self,f):
        num1=self.num*f.num
        den1=self.den*f.den
        return Fraction(num1,den1)
        pass
    
    def div(self,f):
        num1=self.num*f.den
        den1=self.den*self.num
        return Fraction(num1,den1)
    
    
    def __str__(self):
        list=(str(self.num),'/',str(self.den))
        string=''.join(list)
        
        return string



def main():
    f1=Fraction(3,5)
    print('f1 is =',f1)
    print('inverse of f1:',f1.inverse())
    f2=Fraction(2,4)
    print('f2 is =',f2)
    print('inverse of f2:',f2.inverse())
    f3=f1.add(f2)
    print('adding f1+f2 gives:',f3)
    f4=f1.sub(f2)
    print('substracting f1-f2 gives=',f4)
    f5=f1.mul(f2)
    print('multiplying f1*f2 gives =',f5)
    
    f6=f1.div(f2)
    print('dividing f1/f2 gives =',f6)

if __name__== '__main__':
            main()

