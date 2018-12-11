max = int(raw_input())
def largest (arr,r):
  max = arr[0] 
  for i in range(1, r): 
        if arr[i] > max: 
            max = arr[i] 
  return max 
arr = [1,2,3,4,5]
r = len(arr) 
Ans = largest(arr,r) 
print (Ans)
