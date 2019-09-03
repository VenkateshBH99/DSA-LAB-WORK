from mystack import Stack
class Hanoi:
	def __init__(self,numdisk):
		self.numdisk=numdisk
		self.towers=[Stack(),Stack(),Stack()]
		for i in range(numdisk,-1,-1):
			self.towers[0].push(i)
	def moveDisk(self,src,dest):
		self.towers[dest].push(self.towers[src].pop())
	def moveTower(self,n,src,spare,dest):
		if n==0:
			self.moveDisk(src,dest)
			print("Move disk 1 from rod ",src," to rod ",dest)
		else:
			self.moveTower(n-1,src,dest,spare)
			self.moveDisk(src,dest)
			self.moveTower(n-1,spare,src,dest)
def main():
	h=Hanoi(6)
	h.moveTower(6,1,2,3)
if __name__ == '__main__':
	main()