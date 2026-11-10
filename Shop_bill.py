# Ask for one item’s name, price and quantity. Print the subtotal, 
# 5% discount, 17% tax on
# the discounted amount, and the final total, each rounded to 2 decimals.
# Getting Input from the user (name, price and quantity of the item) and calculating the subtotal, discount, tax and final total.
item_name = input("Enter the item name: ")
item_price = float(input("Enter the item price: "))
item_quantity = int(input("Enter the item quantity: ")) 
#calculating the subtotal, discount, tax and final total.
subtotal = item_price * item_quantity
discount = subtotal * 0.05
discounted_amount = subtotal - discount 
tax = discounted_amount * 0.17
final_total = discounted_amount + tax   
print("Item:",item_name)
print("Subtotal: $", round(subtotal, 2))
print("Discount: $", round(discount, 2))
print("Tax: $", round(tax, 2))
print("Final Total: $", round(final_total, 2))  