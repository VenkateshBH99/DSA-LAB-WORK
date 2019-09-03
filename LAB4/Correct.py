S=[None for i in range(100)]

class Node:
	def __init__(self,key=None):
		self.key=key
		self.next=None

def Horner(poly):
	l=len(poly)
	i=l-2
	res=ord(poly[i])
	while i>0:
		i=i-1
		res=res*33+ord(poly[i])
	return res

def horner(poly):
	l=len(poly)
	i=l-1
	res=ord(poly[i])
	while i>0:
		i=i-1
		res=res*33+ord(poly[i])
	return res

def insert1(poly):
	sum=Horner(poly)
	k=sum%100
	poly=poly.strip()
	temp=Node(poly)
	if S[k]:
		current=S[k]
		while current!=None:
			prev=current
			current=current.next
		prev.next=temp
		return S
	else:
		S[k]=temp
		return S

def show(Z,string):
	k=0
	l=len(string)
	j=0
	f=0
	m=0
	while k<100:
		m=0
		if Z[k]:
			current=Z[k]
			while current!=None:
				s=current.key
				i=len(s)
				
				if i is l:
					n=0
					while n<l:
						j=0
						while j<i:
							if j!=n:
								
								if string[j] is s[j]:
									j=j+1
									f=1
								else:
									f=0
									break
							else:
								j=j+1
								continue
							
						if f==1:
							print(current.key)
							break
						n=n+1
				current=current.next
				m=1
			k=k+1
		if m is not 1:
			k=k+1

def inse(Z,string):
	k=0
	l=len(string)
	j=0
	f=0
	m=0
	while k<100:
		m=0
		if Z[k]:
			current=Z[k]
			while current!=None:
				s=current.key
				i=len(s)-1
				if i is l:
					n=0
					while n<l:
						j=0
						while j<l:
							if j<n:
								if string[j] is s[j]:
									f=1
									j=j+1
									continue
								else :
									f=0
									break
							elif j>=n:
									if string[j] is s[j+1]:
										f=1
										j=j+1
										continue
									else:
										f=0
										break

						if f==1:
							print(current.key)
							break
						n=n+1
				current=current.next
				m=1
			k=k+1
		if m is not 1:
			k=k+1

def dele(Z,string):
	k=0
	l=len(string)
	j=0
	f=0
	m=0
	while k<100:
		m=0
		if Z[k]:
			current=Z[k]
			while current!=None:
				s=current.key
				i=len(s)+1
				if i is l:
					n=0
					while n<l:
						j=0
						while j<(i-1):
							if j<n:
								if string[j] is s[j]:
									f=1
									j=j+1
									continue
								else :
									f=0
									break
							elif j>=n:
									if string[j+1] is s[j]:
										f=1
										j=j+1
										continue
									else:
										f=0
										break

						if f==1:
							print(current.key)
							break
						n=n+1
				current=current.next
				m=1
			k=k+1
		if m is not 1:
			k=k+1

def file1():
	path='ispell.dict'
	Spell=open(path,'r')
	c=Spell.readlines()
	s=len(c)
	i=0
	while i<s:
		insert1(c[i])
		i=i+1

def main():
	file1()
	b=input("Enter a string: ")
	print("Suggestions:")
	show(S,b)
	inse(S,b)
	dele(S,b)

if __name__=='__main__':
	main()
	
