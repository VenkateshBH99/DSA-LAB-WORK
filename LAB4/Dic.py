T=[]
S=[]
x=35
class ListNode:
	def __init__(self,val=None):
		self.val=val
		self.next=None

def insert(st,i,Z):
	k=st%len(Z)
	#if k==21182:
		#print(i,' ',st)
	temp=ListNode(i)
	temp.next=Z[k]
	Z[k]=temp
	return
def ispell():
	fh=open("ispell.dict","r")
	l=fh.readlines()
	T=[None for i in range(len(l))]
	for i in l:
		st=ord(i[len(i)-2])
		k=len(i)-2
		while k!=0:
			k=k-1
			st=ord(i[k])+(x*st)
		insert(st,i,T)
		st=0
	fh.close()
	return T
def search(val,Z):
	st=ord(val[len(val)-1])
	k=len(val)-1
	while k!=0:
		k=k-1
		st=ord(val[k])+(x*st)
	j=st%len(Z)
	#print(T[j],'-',j,' ',val,' ',st)
	t=Z[j]
	while t!=None:
		if t.val==(val+'\n'):
			return j
		t=t.next

	return False
def small():
	fh=open("small.dict","r")
	l=fh.readlines()
	S=[None for i in range(len(l))]
	for i in l:
		st=ord(i[len(i)-2])
		k=len(i)-2
		while k!=0:
			k=k-1
			st=ord(i[k])+(x*st)
		insert(st,i,S)
	fh.close()
	return S
def main():
	T=ispell()
	#print(T[10],T[12],T[18021])
	a=input('Enter:')
	print(search(a,T))
	S=small()
	b=input('Enter:')
	print(search(b,S))

if __name__ == '__main__':
	main()
