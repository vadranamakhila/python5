min=int(raw_input())
def smallest(arr,s): 
    min = arr[0]
    for j in range(1, s): 
        if arr[j] > max: 
            min = arr[j] 
    return min
arr = [1,2,3,4,5] 
s = len(arr) 
Ans = smallest(arr,s) 
print (Ans) 
