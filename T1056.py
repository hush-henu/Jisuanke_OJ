n = int(input())
a = 0
b=0
c=0
res =0
for i in range(n):
    x = input().split()
    x = [int(m) for m in x]
    a+=x[0]
    b+=x[1]
    c+=x[2]
    res +=sum(x)
print(a,b,c,res)
