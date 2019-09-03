class Fraction:

    def __init__(self,n,d):
        self.num=n
        self.den=d

    def inverse(self):
        
        return Fraction(self.den,self.num)
        pass
        

    def add(self,f):
        num1=self.num*f.den+f.num*self.den
        den1=self.den*f.den
        return Fraction(num1,den1)
        pass
        

    def subtract(self,f):
        num1=self.num*f.den-f.num*self.den
        den1=self.den*f.den
        return Fraction(num1,den1)
        pass
        

    def multiply(self,f):
       num1=self.num*f.num
       den1=self.den*f.den
       return Fraction(num1,den1)
       pass
       

    def divide(self,f):
        num1=self.num*f.den
        den1=self.den*self.num
        return Fraction(num1,den1)
        pass
        

    def __str__(self):
        list=[str(self.num),'/',str(self.den)]
        string=''.join(list)
        return string

       

def main():
    f1 = Fraction(2,3)
    print('Fraction 1 is', f1)
    f2 = Fraction(3,4)
    print('Fraction 2 is', f2)
    print('The inverse of f1 is', f1.inverse())
    print('The inverse of f2 is', f2.inverse())
    print('f1+f2 is', f1.add(f2))
    print('f1-f2 is', f1.subtract(f2))
    print('f1 * f2 is', f1.multiply(f2))
    print('f1 / f2 is', f1.divide(f2))

if __name__ == '__main__':
    main()