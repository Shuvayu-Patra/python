import math as m
x1 = int(input("Enter x1 :"))
x2 = int(input("Enter x2 :"))
y1 = int(input("Enter y1 :"))
y2 = int(input("Enter y2 :"))
distance = m.sqrt((((x2 - x1)**2)+((y2 - y1) ** 2)))
print ("Distance is : %0.2f" %distance)