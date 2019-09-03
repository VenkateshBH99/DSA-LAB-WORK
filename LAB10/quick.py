def QuickS(A,low,high):
	if low<high:
		pi=partition(A,low,high)
		QuickS(A,low,pi-1)
		QuickS(A,pi+1,high)


def partition(A,low,high):
	i=low-1
	r=A[high]
	for j in range(low,high+1):
		if A[j]<r:
			i=i+1
			A[j],A[i]=A[i],A[j]

	A[i+1],A[high]=A[high],A[i+1]
	return int(i+1)


def main():
	A=[]
	st=input("Enter:")
	l=st.split(' ')
	for i in l:
		A.append(int(i))
	QuickS(A,0,int(len(A)-1))
	print(A)

if __name__ == '__main__':
	main()