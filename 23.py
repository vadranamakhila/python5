min=int(raw_input())
def smallest(arr,r): 
    min = arr[0]
    for i in range(1, r): 
        if arr[i] > max: 
            min = arr[i] 
    return min
arr = [1,2,3,4,5] 
r = len(arr) 
Ans = smallest(arr,r) 
print (Ans) 
