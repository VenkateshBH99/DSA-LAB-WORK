from AVL import AVL

class m:
	def __init__(self):
		self.ma=0
		self.v=None

arr=list(map(int,input("Enter:").rstrip().split()))

r=None
g=AVL()
m=m()
for i in arr:
	r=g.insertNode(r,i,m)
print(m.ma)
if m.ma>len(arr)//2:
	print(m.v)
else:
	print("No")