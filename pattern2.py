row = int(input("Enter no of rows :"))
for i in range(0, row):
    for j in range(0,(2*row)-1):
        if j>=i and j< ((2*row)-1)-i:
         print("*" , end=" ")
        else:
            print(" " , end=" ")
    print("\n")
        