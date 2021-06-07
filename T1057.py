n = int(input())
a = input().split()
a =[int(x) for x in a]
res = (n-2)*180-sum(a)
print(res)