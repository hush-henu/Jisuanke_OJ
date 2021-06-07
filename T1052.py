n = int(input())
a = map(float, input().split())
a = [float(x) for x in a]
print('{:.4f}'.format(sum(a)/n))