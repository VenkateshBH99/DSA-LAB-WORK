class TreeNode:
	def __init__(self,val=None):
		self.val=None
		self.right=None
		self.left=None
		self.height=1

class AVL(object):
	def insert(curr,val):
		if curr==None:
			return TreeNode(val)

		if val<=curr.val:
			curr.left=self.insert(curr.left,val)
		elif val>curr.val:
			curr.right=self.insert(curr.right,val)

		curr.height=1+max(self.getH(curr.left),self.getH(curr.right))
		bal=self.getB(curr)

		if bal>1 and val<curr.left.val:
			return self.rotRight(curr)

		if bal<-1 and val>curr.right.val:
			return self.rotLeft(curr)

		if bal>1 and val > curr.left.val:
			curr.left=self.rotLeft(curr.left)
			return self.rotRight(curr)

		if bal<-1 and val < curr.right.val:
			curr.right=self.rotRight(curr)
			return self.rotLeft(curr)

		return curr

	def delete(curr,val):
		if curr==None:
			return None
		if val<curr.val:
			curr.left=self.delete(curr.left,val)
		elif val>curr.val:
			curr.right=self.delete(curr.right,val)
		else:

			if curr.right==None:
				temp=curr.left
				curr=None
				return temp
			elif curr.left==None:
				temp=curr.right
				curr=None
				return temp

			temp=self.getMin(curr.left)
			curr.val=temp.val
			curr.left=self.delete(curr.left,temp.val)

		curr.height=1+max(self.getH(curr.left),self.getH(curr.right))
		bal=self.getB(curr)

		if bal>1 and self.getB(curr.left)>=0:
			return self.rotRight(curr)

		if bal<-1 and self.getB(curr.right)<=0:
			return self.rotLeft(curr)

		if bal>1 and self.getB(curr.left)<0:
			curr.left=self.rotLeft(curr.left)
			return self.rotRight(curr)

		if bal<-1 and self.getB(curr.right)>0:
			curr.right=self.rotRight(curr.right)
			return self.rotLeft(curr)

		return curr

	def getH(self,curr):
		if curr==None:
			return 0
		return curr.height

	def getB(self,curr):
		if curr==None:
			return 0
		return self.getH(curr.left)-self.getH(curr.right)

	def rotRight(self,z):
		y=z.left
		T3=y.right

		y.right=z
		z.left=T3

		y.height=1+max(self.getH(y.left),self.getH(y.right))
		z.height=1+max(self.getH(z.right),self.getH(z.left))

		return y

	def rotLeft(self,z):
		y=z.right
		T3=y.left

		y.left=z
		z.right=T3

		y.height=1+max(self.getH(y.left),self.getH(y.right))
		z.height=1+max(self.getH(z.right),self.getH(z.left))

		return y


	def getMin(self,curr):
		while curr.left:
			curr=curr.left
		return curr














