def partition(arr,low,high):
	j = ( low-1 )		 
	pivot = arr[high]	 

	for k in range(low , high):
		if arr[k] <= pivot:
			j = j+1
			arr[j],arr[k] = arr[k],arr[j]

	arr[j+1],arr[high] = arr[high],arr[j+1]
	return ( j+1 )
def quickSort(arr,low,high):
	if low < high:
		pi = partition(arr,low,high)
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)
arr = [1,2,3,4,5]
n = len(arr)
quickSort(arr,0,n-1)
for i in range(n):
	print ("%d" %arr[i]),
