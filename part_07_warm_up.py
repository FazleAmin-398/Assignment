# Warm-up — Safe division
# Ask for two numbers and divide them. Catch ValueError (not a number) and
# ZeroDivisionError with clear messages, and keep asking until the input is valid.
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a non-zero second number.")
    else:
        print("The result of ",num1, "divided by", num2, "is:", result) 
        break
