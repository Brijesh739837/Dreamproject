a=int(input("Enter your year="))
print(a)
if a%100==0:
    if a%400==0:
        print("This year is leap year.")
    else:
        print("This is not leap year.")
elif a%4==0:
    print("This is leap year.")
else:
    print("This is not leap year.")