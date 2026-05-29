x=float(input("Enter first number:"))
y=float(input("Enter second number: "))
z=float(input("Enter third number: "))
if x>y and x>z:
    print("x is the biggest number")
elif y>x and y>z:
    print("y is the biggest number")
else:
    print(z," is the biggest number")