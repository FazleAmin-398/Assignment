# Login screens: correct password → enter, wrong → error message.
set_password = "secret123"
user_password = input("Enter your password: ")
if user_password == set_password:
    print("Login successful!")
else:
    print("Error: Incorrect password.")