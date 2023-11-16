def pattern(row):
    for i in range(1,row+1):
        for j in range(1,i+1):
            print(" *", end='')

        print()

row=int(input("Enter numbers of rows \n"))
pattern(row)