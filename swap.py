a = int(input("Enter a number :"))
b = int(input("Enter a number :"))
print("Using third variable:")
print ("Before swap :")
print (" a = " , a)
print (" b = " , b)
c = a
a = b
b = c
print ("After swap :")
print (" a = " , a)
print (" b = " , b)

print("Without Using third variable:")
print ("Before swap :")
print (" a = " , a)
print (" b = " , b)
a = a+b
b = a-b
a = a-b
print ("After swap :")
print (" a = " , a)
print (" b = " , b)

print ("Using Bitwise Operator :")
print ("Before swap :")
print (" a = " , a)
print (" b = " , b)
a = a^b
b = a^b
a = a^b
print ("After swap :")
print (" a = " , a)
print (" b = " , b)

