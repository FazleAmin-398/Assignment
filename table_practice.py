#table practice
table=int(input("Enter the number for which you want to print the multiplication table: "))
for i in range(1, 11):
    result=table*i
    print(table, "x", i, "=", result)