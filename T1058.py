m,n = map(int,input().split())
sfddsaf =0
for i in range(m,n+1):
    if i & 1:
        sfddsaf+=i
print(sfddsaf)
