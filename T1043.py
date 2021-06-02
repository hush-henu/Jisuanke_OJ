import math

a,b =input().split()
a = float(a)
base =8
if a<=1000:
    base=8
else:
    base+= math.ceil((a-1000)/500.)*4
if b=='y':
    print(base+5)
else:
    print(base)
