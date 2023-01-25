row = int(input("Enter no of rows:"))
a = 1
for i in range(0,row):
    for j in range(0 , i+1):
        print (a , end=" ")
        a += 1
    print("\n")
