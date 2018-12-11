r=int(raw_input())
rev=0
while(r>0):
    remainder=r%10
    rev=rev*10+remainder
    r=r/10
print rev    
