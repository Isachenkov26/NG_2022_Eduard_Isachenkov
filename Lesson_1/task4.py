import math

a = float(input("Enter a number: "))
b = float(input("Enter b number: "))
c = float(input("Enter c number: "))
if(((b * b) - 4 * a * c) > 0):
    print("x1 = ", (-b + math.sqrt((b * b) - 4 * a * c))/(2 * a))
    print("x2 = ", (-b - math.sqrt((b * b) - 4 * a * c))/(2 * a))
elif(((b * b) - 4 * a * c) == 0):
    print("x = ", -(b / (2 * a)))
else:
    print("D < 0")
input("Click enter to exit")