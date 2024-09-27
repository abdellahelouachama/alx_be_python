FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


temperature = int(input("Enter the temperature to convert: "))
if type(temperature) == int:

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()
    if unit == "C":
        Fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{float(temperature)}°C is {float(Fahrenheit)}°F")

    elif unit == "F":
        Celsius = convert_to_celsius(temperature)
        print(f"{float(temperature)}°F is {float(Celsius)}°C")
    
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
   
else:
    print("Invalid temperature. Please enter a numeric value.")    