import math

a = float(input("Enter a number: "))
b = float(input("Enter b number: "))
action = float(input("\n1 - addition\n2 - subtraction\n3 - multiplication\n4 - division\n5 - square\n6 - root\nChoose an expression: "))
if(action == 1):
    print(a+b)
elif(action == 2):
    print(a-b)
elif(action == 3):
    print(a*b)
elif(action == 4):
    print(a/b)
elif(action == 5):
    print("Square with a number: ", a*a, "\nSquare with b number: ", b*b)
elif(action == 6):
    print("Root with a number: ", math.sqrt(a), "\nRoot with b number: ", math.sqrt(b))
else:
    print("You entered incorrectly")
input("Click to exit enter ")