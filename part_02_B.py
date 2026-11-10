# Cinema or bus tickets: children and seniors pay less
age = int(input("Enter your age: "))
if age < 12:
    print("Child ticket price: $5.00")
elif age >= 65:
    print("Senior ticket price: $7.00")
else:
    print("Adult ticket price: $10.00")