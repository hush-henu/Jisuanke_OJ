import math

n,x,y = map(int,input().split())

sum = math.ceil(y/x)
res  = n-sum
print(res if res>0 else 0)