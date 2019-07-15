a = int(input("Enter first number"))
b = int(input("Enter Second number"))
c = int(input("Enter Third number"))
if a>b:
    if a>c:
        print("a is greater=",a)
elif b>c:
    if b>a:
        print("b is greater=",b)
else:
    print("c is greater=",c)