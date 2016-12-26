


def countInversion(arr):
	temp = []
	return countsort(arr,temp,0,len(arr)-1)


def countsort(arr,temp,left,right):
	if right <=left: 
		return 0

	mid = (right + left)//2

	ans1 = countsort (arr, temp, left, mid)
	ans2 = countsort (arr, temp, mid+1,right)
	ans3 = mergecount(arr, temp, left, mid+1,right)

	return ans1 + ans2 + ans3 

def mergecount(arr,temp,left,mid,right):
	# i is index for left array, mid is index for right array
	# k is index for merged array 
	i,j,k = left,mid,left
	numberOfinversions = 0
	while i <= mid-1 and j <= right:
		if arr[i] <= arr[j]:
			temp[k] = arr[i]
			k += 1
			i += 1
		else:
			temp[k] = arr[j]	 	
			numberOfinversions += mid - i
			k += 1
			j += 1 

	while i <= mid -1:
		temp[k] = arr[i]
		k += 1
		i += 1

	while j <= right:
		temp[k] = arr[j]
		k += 1
		j += 1
	
	for i in range(left, right+1):
		arr[i] = temp[i]
	return numberOfinversions	 			

test = [1,20,6,4,5]
k = countInversion(test)
print("Number of inversions are 5 and my code said ", k)
