# Warm-up — Student ID card
# Ask for name, age, class and city, then print a neat card. Also print the type of each value
# with type() 

name = input("Enter your name: ")
age = int(input("Enter your age: "))
class_name = input("Enter your class: ")
city = input("Enter your city: ")

print(f"Name: {name}", type(name))
print(f"Age: {age}", type(age))
print(f"Class: {class_name}", type(class_name))
print(f"City: {city}", type(city))

# print(f"Type of name: {type(name)}")
# print(f"Type of age: {type(age)}")
# print(f"Type of class: {type(class_name)}")
# print(f"Type of city: {type(city)}")