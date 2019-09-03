class ListNode:
	def __init__(self,value=None,next=None,key=None):
		self.value=value
		self.next=next
		self.key=key

T=[None for i in range(30)]
def Com(s):
	l=len(s)
	i=0
	sum=0
	while i!=l:
		sum=sum+ord(s[i])
		i=i+1
	return sum
def insert(sum,val):
	k=sum%30
	temp=ListNode()
	temp.value=val
	temp.next=None
	temp.key=sum
	if T[k]==None:
		T[k]=temp
	else:
		art=T[k].next
		while art!=None:
			art=art.next
			art.next=temp

def search(val):
	sum=Com(val)
	k=sum%30
	temp=T[k]
	if T[k]==None:
		return print("Search unsuccessfull")
	else:
		while temp.next!=None:
			if temp.value==val:
				return print("Search Successfull")
			temp=temp.next
		if temp.value==val:
			return print("Search Successfull")
		return print("Search unsuccessfull")
def key(T):
	i=0
	while i!=30:
		if T[i]!=None:
			print(i)
		i=i+1
	return

def main():
	while True:
		ch=int(input("Enter\n1 for inserting\n2 for searching\n3 for printing key values\n4 for exit\n"))
		if ch==1:
			inp=input("Enter the input")
			sum=Com(inp)
			insert(sum,inp)
		elif ch==2:
			s=input("Enter the value to search")
			search(s)
		elif ch==3:
			key(T)
		elif ch==4:
			break
		else:
			print("Invalid choice")

	
if __name__=='__main__':
	main()








