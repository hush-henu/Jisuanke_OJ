n = int(input())
a = input().split()
a = [int(x) for x in a]
print(max(a)-min(a))