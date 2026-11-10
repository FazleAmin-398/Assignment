# Ask for a temperature in Celsius and a distance in kilometres. Print Fahrenheit ( C × 9/5
# + 32 ), Kelvin, miles ( km × 0.621371 ) and metres, using f-strings with 1 decimal place
# getting input from the user for the temperature in celcius and distand in kilometers
celsius = float(input("Enter the temperature in Celsius: "))
kilometres = float(input("Enter the distance in kilometres: "))
#formul as for converting celsius to fahrenheit, kelvin and kilometres to miles and metres
fahrenheit = celsius * 9/5 + 32
kelvin = celsius + 273.15
miles = kilometres * 0.621371
metres = kilometres * 1000
#printing the converted values with 1 decimal place using f-strings
print(f"Fahrenheit: {fahrenheit:.1f}")
print(f"Kelvin: {kelvin:.1f}")
print(f"Miles: {miles:.1f}")
print(f"Metres: {metres:.1f}")