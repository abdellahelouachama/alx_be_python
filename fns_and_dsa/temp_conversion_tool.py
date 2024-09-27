CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9 

def convert_to_celsius(fahrenheit):
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    print(f"{round(fahrenheit, 2)}°F is {float(celsius)}°C")






def onvert_to_fahrenheit(celsius):
    fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32
    print(f"{round(celsius, 2)}°C is {float(fahrenheit)}°F")




temperature = int(input("Enter the temperature to convert: "))
if type(temperature) == int:
    print("nvalid temperature. Please enter a numeric value.")

    choise = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()

    if choise == "F":
        convert_to_celsius(temperature)
    elif choise == "C":
        onvert_to_fahrenheit(temperature)
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")    
else:
    print("Invalid temperature. Please enter a numeric value.")