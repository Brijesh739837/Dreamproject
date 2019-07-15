from math import *
'''num=int(input("Enter ny number"))
print(num)
i=2
while i<=num-1:
    if num%2==0:
        print("not prime")
        break
    else:
        print("prime no")
        break
    i=i+1'''

num=int(input("Enter ny number"))
print(num)
i=2
while i<=num-1:
    if num%2==0:
        print("not prime")
        break
    i=i+1
else:
    print("prime no")

num=int(input("Enter ny number"))
print(num)
i=2
while i<=sqrt(num):
    if num%2==0:
        print("not prime")
        break
    i=i+1
else:
    print("prime no")
