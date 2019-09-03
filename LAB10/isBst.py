class TreeNode:
	def __init__(self,val):
		self.val=val
		self.right=None
		self.left=None

def check(curr):
	if curr.left==None and curr.right==None:
		return True

	if curr.right==None:
		if curr.val>=curr.left.val:
			return check(curr.left)
		else:
			return False

	elif curr.left==None:
		if curr.val<curr.right.val:
			return check(curr.right)
		else:
			return False

	if curr.val>=curr.left.val and curr.val<curr.right.val:
		return (check(curr.left) and check(curr.right))
	else:
		return False

def main():
	root=TreeNode(6)
	root.right=TreeNode(8)
	root.right.left=TreeNode(7)
	root.left=TreeNode(4)
	root.left.left=TreeNode(3)
	root.left.right=TreeNode(5)
	if check(root):
		print("BST")
	else:
		print("Not Bst")

if __name__=='__main__':
	main()