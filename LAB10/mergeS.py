
def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        mergeSort(L)
        mergeSort(R)

        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i=i+1
            else:
                arr[k]=R[j]
                j=j+1
            k=k+1

        while i<len(L):
            arr[k]=L[i]
            i=i+1
            k=k+1

        while j<len(R):
            arr[k]=R[j]
            j=j+1
            k=k+1



def prin(arr):
    for i in arr:
        print(i,end=' ')
    print()

def main():
    arr=[]
    ele=input('Enter the numbers:')
    ar=ele.split(' ')
    for i in ar:
        arr.append(int(i))
    mergeSort(arr)
    prin(arr)

if __name__=='__main__':
    main()
