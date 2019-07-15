a = int(input("Enter the marks of first Subject : "))
b = int(input("Enter the marks of second Subject : "))
c = int(input("Enter the marks of third Subject : "))
d = int(input("Enter the marks of fourth Subject : "))
e = int(input("Enter the marks of fifth Subject : "))
total=a+b+c+d+e
perc=(total/500)*100
if perc>=0 and perc<33:
    print("Failed")
elif perc>=33 and perc<45:
    print("Third divison")
elif perc>=45 and perc<60:
    print("Second divison")
else:
    print("First divison")

