# An ATM gives you 3 tries to enter the right PIN (while loop).
correct_pin="4321"
tries=3
while tries>0:
    user_pin=input("Enter your PIN: ")
    if user_pin==correct_pin:
        print("Access granted.")

    else:
        tries=tries-1
        if tries>0:
            print("Incorrect PIN. You have", tries, "tries left.")
        else:
            print("Sorry, you have exceeded the number of tries your card is blocked.")