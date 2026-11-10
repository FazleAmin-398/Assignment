# Challenge — Electricity bill
# Ask for units used. The first 100 units cost Rs 10 each, the next 100 cost Rs 15, and every
# unit above 200 costs Rs 20. Add Rs 50 fixed charges. Print the total. Example: 250 units →
# 1000 + 1500 + 1000 + 50 = Rs 3550
units = int(input("Enter the number of units used: "))
# first 100 cost Rs 10 Each,
if units <= 100:
    total_cost = units * 10
    #the next 100 cost Rs 15 101 to 200.
elif units <= 200:
    total_cost = (100 * 10) + ((units - 100) * 15)
    #and every unit above 200 costs Rs 20. 
else:
    total_cost = (100 * 10) + (100 * 15) + ((units - 200) * 20)
    # Add Rs 50 fixed charges.
total_cost += 50  # Add fixed charges
print("Total electricity bill: Rs", total_cost)