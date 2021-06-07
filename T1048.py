a,b,c = input().split()
a= int(a)
b= int(b)

if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    if b == 0:
        print("Divided by zero!")
    print(int(a/b))
else:
    print("Invalid operator!")