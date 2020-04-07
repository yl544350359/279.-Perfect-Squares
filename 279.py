import math
# n is a positive integer
n=12

savedata=[0]*(n+1)
savedata[1]=1
for i in range(2,n+1):
    maxs=math.floor(pow(i,0.5))
    candidate=[]
    for x in range(1,maxs+1):
        candidate.append(savedata[i-x*x])
    savedata[i]=min(candidate)+1
    
print(savedata[n])