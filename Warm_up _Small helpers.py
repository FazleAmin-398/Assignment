# Write area_of_circle(r) , is_even(n) and greet(name, lang="en") where lang can
# be "en" or "ur" (“Salaam”). Call each one three times.
def area_of_circle(r):
    pi = 3.14159
    area = pi * r ** 2
    return area


def is_even(n):
    return n % 2 == 0


def greet(name, lang="en"):
    if lang == "ur":
        return f"Salaam, {name}!"
    else:
        return f"Hello, {name}!"


print(area_of_circle(2))
print(area_of_circle(3))
print(area_of_circle(4))

print(is_even(2))
print(is_even(3))
print(is_even(10))

print(greet("Ali"))
print(greet("Ayesha", "en"))
print(greet("Bilal", "ur"))
   