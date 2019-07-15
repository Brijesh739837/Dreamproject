#Simple interest
'''p=int(input("Enter your amount="))
n=int(input("Enter time"))
r=int(input("Enter your rate"))
si=(p*n*r)/100
total=p+si
print(tatal)'''


#Compond interest

p=int(input("Enter your amount="))
n=int(input("Enter time"))
r=int(input("Enter your rate"))
a=(p*(1+(r/100))**n)
interest=a+p
print(interest)