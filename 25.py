median=int(raw_input())
n = [1,2,3,4,5]
n.sort()
length = len(n)
if (length % 2 == 0):
    median = (n[(length)//2] + n[(length)//2-1]) / 2
else:
    median = n[(length-1)//2]
print(median)
