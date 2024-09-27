FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    global unit
    unit = 'C'
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    print(f"{float(fahrenheit)}°C is {float(celsius)}°{unit}")
    



def onvert_to_fahrenheit(celsius):
    global unit
    unit = 'F'
    fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32
    print(f"{float(celsius)}°C is {float(fahrenheit)}°{unit}")




temperature = int(input("Enter the temperature to convert: "))
if type(temperature) == int:

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()

    if unit == "F":
        convert_to_celsius(temperature)
    elif unit == "C":
        onvert_to_fahrenheit(temperature)
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")    
else:
    print("Invalid temperature. Please enter a numeric value.")