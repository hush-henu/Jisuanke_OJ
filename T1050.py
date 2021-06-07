a = int(input())

b = []
for i in range(a):
    b.append(int(input()))
print('{:.2f}'.format(sum(b)/a))