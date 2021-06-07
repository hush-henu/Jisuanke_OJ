n = int(input())
a = []
for i in range(n):
    a.append(float(input()))

print('{} {:.5f}'.format(int(sum(a)), sum(a )/ n))
