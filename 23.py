min=int(raw_input())
def smallest(arr,n): 
    min = arr[0]
    for i in range(1, n): 
        if arr[i] > max: 
            min = arr[i] 
    return min
arr = [1,2,3,4,5] 
n = len(arr) 
Ans = smallest(arr,n) 
print (Ans) 
