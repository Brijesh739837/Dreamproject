from math import *
a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))
c = int(input("Enter the value of c"))

d=(b*b-4*a*c)
if d==0:
    print("Roots are equal")
    x1=-b/(2*a)
    x1=x2
    print("X1=",x1,"X2=",x2)
elif d>0:
    print("Roots are unequal")
    x1=(b+sqrt(d))/(2*a)
    x2=(-b+sqrt(d)/(2*a))
    print("X1=",x1,"X2=",x2)
else:
    print("Roots are imaginary")